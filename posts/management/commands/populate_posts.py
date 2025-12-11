from django.core.management.base import BaseCommand
from posts.models import Post
from django.utils import timezone


SAMPLE = [
    ("Welcome to the Store", "This is a sample post to welcome visitors."),
    ("New Arrivals", "Check out our latest products and offers."),
    ("Holiday Sale", "Don't miss the special discounts this season."),
    ("Restocked", "Popular items have been restocked today."),
    ("Member Benefits", "Sign up for exclusive member-only deals."),
    ("Shipping Info", "We ship worldwide with tracking available."),
    ("Customer Stories", "See what our customers are saying."),
    ("Sustainability", "How we source eco-friendly products."),
    ("Tech Tips", "Useful tips for maintaining your electronics."),
    ("Contact Us", "We're here to help — reach out anytime."),
]


class Command(BaseCommand):
    help = 'Populate the database with sample Post entries.'

    def handle(self, *args, **options):
        created = 0
        for title, content in SAMPLE:
            obj, _ = Post.objects.get_or_create(
                title=title,
                defaults={'content': content, 'created_at': timezone.now()},
            )
            if obj:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Created/ensured {len(SAMPLE)} sample posts.'))
