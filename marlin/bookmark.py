from marlin.manage import ManageBookmark
from marlin.styles import label, color
from pathlib import Path
import click


@click.command()
@click.argument("bookmark_name")
@click.argument("bookmark_path", default=Path.cwd())
def main(bookmark_name, bookmark_path):
    """
    Bookmark the current folder.
    """
    # create the bookmark object and load the bookmarks
    bookmark_object = ManageBookmark(bookmark_name, str(bookmark_path))
    bookmark_object.create_marlin_folder()
    all_bookmarks = bookmark_object.list_bookmark()

    if bookmark_name in all_bookmarks:
        click.confirm(exist_msg(bookmark_name), abort=True)
    else:
        click.confirm(bookmark_msg(bookmark_name), abort=True)

    # create new bookmark
    bookmark_object.add_bookmark()
    click.echo(bookmarked_msg(bookmark_name))


def exist_msg(bookmark_name):
    bmk_exist = "Bookmark already exists. Overwrite"
    return "\n{} {} {}?".format(
        label("info"), bmk_exist, color("yellow", bookmark_name)
    )


def bookmark_msg(bookmark_name):
    return "\n{} {} {}".format(
        label("info"), "Do you want to bookmark", color("yellow", bookmark_name)
    )


def bookmarked_msg(bookmark_name):
    return "{} {} {}".format(
        label("good"), color("yellow", bookmark_name), "has been bookmarked."
    )


if __name__ == "__main__":
    main()
