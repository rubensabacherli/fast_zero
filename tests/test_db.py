from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Rubens', email='rubens@rubens.com', password='123123'
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'rubens@rubens.com')
    )

    assert result.username == 'Rubens'
