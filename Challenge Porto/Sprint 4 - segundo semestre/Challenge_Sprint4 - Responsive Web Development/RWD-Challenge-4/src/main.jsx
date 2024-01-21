import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

import {createBrowserRouter, RouterProvider} from "react-router-dom";

import Home from "./routes/Home.jsx";
import Sac from "./routes/Sac.jsx"
import ErrorPage from './routes/ErrorPage.jsx';
import RM from './routes/RM.jsx'
import Cadastro from './routes/Cadastro.jsx';
import Logar from './routes/Logar.jsx';
import Cotacao from './routes/Cotacoes.jsx';
import Pagamentos from './routes/Pagamentos.jsx';



const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage/>,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "Sac",
        element: <Sac/>,
      },
      {
        path: "RM",
        element: <RM/>,
      },
      {
        path: "Cadastro",
        element: <Cadastro/>,
      },
      {
        path: "Logar",
        element: <Logar/>,
      },
      {
        path: "Cotacao",
        element: <Cotacao/>,
      },
      {
        path: "Pagamentos",
        element: <Pagamentos/>,
      },
    ],
  },
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)
