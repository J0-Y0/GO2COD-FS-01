from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Post, Comment, Report, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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
            {"fields": ("title", "slug", "image", "category", "excerpt", "content")},
        ),
        (
            "Status & Author",
            {
                "fields": ("status", "author", "published_date"),
                "classes": ("collapse",),  # Makes the section collapsible
            },
        ),
        (
            "User Interaction",
            {
                "fields": ("favorite", "liked", "disliked", "tags"),
            },
        ),
    )


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin):
    list_display = ("author", "post", "content", "published_date", "status")
    list_filter = ("status", "published_date", "post")
    search_fields = ("author__username", "content", "post__title")
    date_hierarchy = "published_date"
    ordering = ("-published_date",)
    raw_id_fields = ("post", "parent")  # Optimize ForeignKey field selection

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
class ReportAdmin(admin.ModelAdmin):
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
        (
            "Date",
            {
                "fields": ("published_date",),
                "classes": ("collapse",),  # Makes the section collapsible
            },
        ),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
