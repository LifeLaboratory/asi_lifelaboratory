from app.route.auth.route import Auth
from app.route.profile.route import Profile
from app.route.register.route import Register

from app.route.route_user_category import UserCategory
from app.route.category.route import Category

from app.route.document.route import Document, GetDocument
from app.route.documents.route import Documents

from app.route.lesson.route import Lesson, GetLesson

from app.route.project.route import Project, GetProject, GetProjectBudget, GetProjectCategory
from app.route.projects.route import Projects

from app.route.ads.route import Ads

from app.route.cv.route import GetCv, Cv
from app.route.investors.route import Investors

from app.route.budget.route import Budget, GetBudget
from app.route.print_form.route import PrintForm, GetPrintForm


ROUTES = {
    '/register': Register,
    '/auth': Auth,
    '/profile/<int:id_user>': Profile,

    '/user/<int:id_user>/category': UserCategory,
    '/category/<int:id_category>': Category,

    '/document': Document,
    '/document/<int:id_document>': GetDocument,
    '/documents': Documents,

    '/project': Project,
    '/project/filter': Projects,
    '/project/<int:id_project>': GetProject,
    '/project/<int:id_project>/category': GetProjectCategory,
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

    '/print_form': PrintForm,
    '/print_form/<int:id_user>': GetPrintForm,
}
