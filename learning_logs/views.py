from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

from .refratorization import check_topic_owner

# Create your views here.
def index(request):
    """Main page of learning_logs application."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Displaying all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('dateAdded')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Displays single topic with its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Assuring that its user's topic
    check_topic_owner(topic, request)

    entries = topic.entry_set.order_by('-dateAdded')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add new topic."""
    if request.method != 'POST':
        # No data was transfered, an empty form need to be created.
        form = TopicForm
    else:
        # Data was transfered with POST, they need to be handled.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    
    # Displaying an empty form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Adding new entry for a specific topic."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # No data was transfered, an empty form need to be created.
        form = EntryForm()
    else:
        # Data was transfered with POST, they need to be handled.
        form = EntryForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    # Displaying an empty form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # Initial request, filling form with recent entry content.
        form = EntryForm(instance=entry)
    else:
        # Data was transfered with POST, they need to be handled.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)