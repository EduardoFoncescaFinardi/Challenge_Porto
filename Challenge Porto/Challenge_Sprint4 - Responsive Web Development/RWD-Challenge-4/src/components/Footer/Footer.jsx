import './Footer.css'
import logo from '../../images/portologo.png'
import { Link } from "react-router-dom";

const Footer = () => {
    return(
        <div className='footer'>
            <img src={logo} alt='logo'></img>
            <h3>© 2023 Todos os direitos reservados</h3>
            <Link to="/Rm">RM's</Link>
        </div>
    );
};

export default Footer;