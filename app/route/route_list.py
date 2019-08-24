from app.route.route_auth import Auth
from app.route.route_profile import Profile
from app.route.route_register import Register

from app.route.route_user_category import UserCategory
from app.route.route_category import Category

from app.route.route_document import Document, GetDocument
from app.route.route_documents import Documents

from app.route.route_project import GetProject, Project
from app.route.route_projects import Projects

from app.route.route_ads import Ads

from app.route.route_cv import GetCv, Cv


ROUTES = {
    Register: '/register',
    Auth: '/auth',
    Profile: '/profile/<int:id_user>',

    UserCategory: '/user/category/<int:id_user>',
    Category: '/category/<int:id_category>',

    Document: '/document',
    GetDocument: '/document/<int:id_document>',
    Documents: '/documents',

    Project: '/project',
    Projects: '/project/filter',
    GetProject: '/project/<int:id_project>',

    Ads: '/ads',

    Cv: '/cv',
    GetCv: '/cv/<int:id_user>',
}
