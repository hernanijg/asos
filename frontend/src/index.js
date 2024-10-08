import React from 'react';
import ReactDOM from 'react-dom/client';

import reportWebVitals from '@/reportWebVitals';
import { RouterProvider } from 'react-router-dom';
import router from '@/routers/router';

`Pongo esto aca de prueba`
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

reportWebVitals();
