from src.app.domain.models import Tasks


def test_tasks_instance_creation():
    task = Tasks("Title", False)
    assert isinstance(task, Tasks)
    assert task.title == "Title"
    assert task.completed is False


def test_tasks_to_camel_case():
    assert Tasks.to_camel_case("title") == "title"
    assert Tasks.to_camel_case("Title") == "title"
    assert Tasks.to_camel_case("title_title") == "titleTitle"
    assert Tasks.to_camel_case("title title") == "titleTitle"
    assert Tasks.to_camel_case("title-title") == "titleTitle"
    assert Tasks.to_camel_case("title-title-title") == "titleTitleTitle"
    assert Tasks.to_camel_case("title_title_title") == "titleTitleTitle"
    assert Tasks.to_camel_case("title-title-title") == "titleTitleTitle"
    assert Tasks.to_camel_case("title title title") == "titleTitleTitle"
