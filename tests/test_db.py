from fast_zero.models import User


def test_create_user():
    user = User(
        username='Rubens', email='rubens@rubens.com', password='123123'
    )

    assert user.username == 'Rubens'
