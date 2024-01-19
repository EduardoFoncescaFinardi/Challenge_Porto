import { Outlet } from 'react-router-dom'
import Navbar from './components/Navbar/Navbar'
import Linha from './components/Linha/Linha'
import Footer from './components/Footer/Footer'


function App() {
  return (
    <>
      <Navbar/>
      <Linha/>
      <Outlet/>
      <Linha/>
      <Footer/>
    </>
  )
}

export default App
