from app.route.route_auth import Auth
from app.route.route_profile import Profile
from app.route.route_register import Register
from app.route.route_info_user import InfoUser


ROUTES = {
    Register: '/register',
    Auth: '/auth',
    Profile: '/profile/<int:id_user>',
    InfoUser: '/info/<int:id_nom>/<string:id_user>',
}
