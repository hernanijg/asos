import {createBrowserRouter} from 'react-router-dom'

// RUTAS AND PAGES
import * as view from '@/views'
import * as ROUTES from '@/constants/routes'

const router = createBrowserRouter([
    {
        path: ROUTES.HOME,
        element: <view.Home />
    },
    {
        path: ROUTES.MEN,
        element: <> MEN </>
    },
    {
        path: ROUTES.WOMEN,
        element: <> WOMEN </>
    },
    {
        path: ROUTES.ACCOUNT,
        element: <> ACCOUNT</>
    }, 
    {
        path: ROUTES.ORDERHISTORY,
        element: <> ORDER </>
    },
    {
        path: ROUTES.LIKEPRODUCT,
        element: <> LIKE PRODUCT</>
    },
    {
        path: ROUTES.CAR,
        element: <> CAR </>
    }
])

export default router