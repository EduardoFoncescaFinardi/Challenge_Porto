import { Link } from "react-router-dom";
import imglogo from '../../images/portologo.png'
import {FiUser} from "react-icons/fi" ;
import './Navbar.css'


const Navbar = () => {
    return(
        <div className="header">
            <div className="logo-header">
                <Link to="/"><img src={imglogo}></img></Link>
            </div>
            <nav className="nav">
                <div className="LinkHome">
                    <Link to="/">Home</Link>
                </div>
                <div className="LinkSac">
                    <Link to="/Sac">Sac</Link>
                </div>
            </nav>
            <div className="login-wrapper">
                <div className='icon'>
                    <FiUser size={35}/>
                 </div>
                <div className='login'>
                    <Link to="/Logar">Entrar</Link>
                    <Link to="/Cadastro">Cadastrar-se</Link>
                </div>
            </div>
        </div>
    );
};

export default Navbar;