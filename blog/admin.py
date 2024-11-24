from django.contrib import admin
from unfold.admin import ModelAdmin
from mptt.admin import MPTTModelAdmin
from .models import Post, Comment, Report, Category

from taggit.models import Tag

from taggit.admin import TagAdmin as DefaultTagAdmin


@admin.register(Post)
class PostAdmin(ModelAdmin):
    compressed_fields = True
    # Display submit button in filters
    list_filter_submit = True

    # Display changelist in fullwidth
    list_fullwidth = True

    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    list_display = ("title", "author", "status", "published_date")
    list_filter = ("status", "author", "category", "published_date")
    search_fields = ("title", "content", "author__username")
    prepopulated_fields = {
        "slug": ("title",)
    }  # Automatically generate the slug from the title
    ordering = ("-published_date",)
    date_hierarchy = "published_date"
    list_editable = ("status",)
    filter_horizontal = ("favorite", "liked", "disliked")  # For ManyToMany fields
    autocomplete_fields = ("category", "author")  # For ForeignKey fields

    # Grouping fields using fieldsets
    fieldsets = (
        (
            "Basic Information",
            {
                "classes": ["tab"],
                "fields": (
                    "title",
                    ("slug", "image"),
                    "category",
                    "excerpt",
                    "content",
                ),
            },
        ),
        (
            "Status & Author",
            {
                "classes": ["tab"],
                "fields": ("status", "author", "published_date"),
                # "classes": ("collapse",),  # Makes the section collapsible
            },
        ),
        (
            "User Interaction",
            {
                "classes": ["tab"],
                "fields": ("favorite", "liked", "disliked", "tags"),
            },
        ),
    )


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    compressed_fields = True

    list_display = (
        "author",
        "post",
        "parent",
        "content",
        "published_date",
        "status",
    )
    list_filter = ("status", "published_date", "post")
    search_fields = ("author__username", "content", "post__title")
    date_hierarchy = "published_date"
    ordering = ("-published_date",)
    raw_id_fields = ("post", "parent")  # Optimize ForeignKey field selection
    autocomplet_field = ["post"]

    # Grouping fields using fieldsets
    fieldsets = (
        ("Comment Details", {"fields": ("author", "post", "content", "parent")}),
        (
            "Status & Interaction",
            {
                "fields": ("status", "liked"),
                "classes": ("collapse",),  # Makes the section collapsible
            },
        ),
    )


@admin.register(Report)
class ReportAdmin(ModelAdmin):
    compressed_fields = True

    list_display = ("author", "post", "type", "published_date")
    list_filter = ("type", "published_date")
    search_fields = ("author__username", "post__title", "detail")
    date_hierarchy = "published_date"
    ordering = ("-published_date",)
    autocomplete_fields = (
        "post",
        "author",
    )  # For better performance with ForeignKey fields

    # Grouping fields using fieldsets
    fieldsets = (
        (
            "Report Details",
            {"fields": ("author", "post", "type", "otherDescription", "detail")},
        ),
        # (
        #     "Date",
        #     {
        #         "fields": ("published_date",),
        #         "classes": ("collapse",),  # Makes the section collapsible
        #     },
        # ),
    )


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ["name", "last_updated"]
    search_fields = ["name"]


admin.site.unregister(Tag)


@admin.register(Tag)
class tagAdmin(ModelAdmin):
    list_display = ["name"]
