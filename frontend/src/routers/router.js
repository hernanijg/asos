import {createBrowserRouter} from 'react-router-dom'

// RUTAS AND PAGES
import * as view from '../views'
import * as ROUTES from '../constants/routes'

const router = createBrowserRouter([
    {
        path: ROUTES.HOME,
        element: <view.Home />
    }
])

export default router