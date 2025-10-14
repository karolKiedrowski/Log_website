from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    """Main page of learning_logs application."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Displaying all topics."""
    topics = Topic.objects.order_by('dateAdded')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Displays single topic with its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-dateAdded')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)