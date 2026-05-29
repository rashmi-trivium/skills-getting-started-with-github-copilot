def test_get_activities_returns_success_and_dictionary(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)


def test_get_activities_includes_expected_activity_keys(client):
    # Arrange
    url = "/activities"
    expected_keys = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Tennis Club",
        "Art Studio",
        "Drama Club",
        "Debate Team",
        "Science Club",
    }

    # Act
    response = client.get(url)

    # Assert
    activities = response.json()
    assert expected_keys.issubset(set(activities.keys()))


def test_get_activities_entry_contains_required_fields(client):
    # Arrange
    url = "/activities"
    activity_name = "Chess Club"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(url)

    # Assert
    activity = response.json()[activity_name]
    assert required_fields.issubset(set(activity.keys()))
    assert isinstance(activity["participants"], list)
