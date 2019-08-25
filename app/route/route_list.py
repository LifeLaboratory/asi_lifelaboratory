from app.route.route_auth import Auth
from app.route.route_profile import Profile
from app.route.route_register import Register

from app.route.route_user_category import UserCategory
from app.route.route_category import Category

from app.route.route_document import Document, GetDocument
from app.route.route_documents import Documents

from app.route.route_lesson import Lesson, GetLesson

from app.route.route_project import Project, GetProject, GetProjectBudget
from app.route.route_projects import Projects

from app.route.route_ads import Ads

from app.route.route_cv import GetCv, Cv
from app.route.route_investors import Investors

from app.route.route_budget import Budget, GetBudget


ROUTES = {
    '/register': Register,
    '/auth': Auth,
    '/profile/<int:id_user>': Profile,

    '/user/category/<int:id_user>': UserCategory,
    '/category/<int:id_category>': Category,

    '/document': Document,
    '/document/<int:id_document>': GetDocument,
    '/documents': Documents,

    '/project': Project,
    '/project/filter': Projects,
    '/project/<int:id_project>': GetProject,
    '/project/<int:id_project>/budget': GetProjectBudget,

    '/ads': Ads,

    '/cv': Cv,
    '/cv/<int:id_cv>': GetCv,

    '/lessons': Lesson,
    '/lesson/<int:id_lesson>': GetLesson,

    '/budget': Budget,
    '/budget/<int:id_user>': GetBudget,
    # '/budget/<int:id_user>/<int:id_project>': GetBudgetProject,

    '/investors': Investors,
}
