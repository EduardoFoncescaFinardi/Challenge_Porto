import './Assistencia.css'
import icon1 from '../../images/icon1.png'
import icon2 from '../../images/icon2.png'
import icon3 from '../../images/icon3.png'
import icon4 from '../../images/icon4.png'

const Assistencia = () => {
    return(
        <div className="container">
            <div className='headerAssistencias'><h2>Assistências</h2></div>
            <div className='body'>
                <div className='block'>
                    <img className="icon1" src={icon1} alt="Roubo"></img>
                    <h3>ROUBO</h3> 
                    <p className='up'>Segurança contra</p>
                    <p>Furto e roubo.</p>
                </div>
                <div className='block'>
                    <img className="icon2" src={icon2} alt="Acidentes"></img>
                    <h3>ACIDENTES</h3> 
                    <p className='up'>Segurança contra</p>
                    <p>acidentes pessoais.</p>
                </div>
                <div className='block'>
                    <img className="icon3" src={icon3} alt="Quebrado"></img>
                    <h3>DANOS</h3> 
                    <p className='up'>Segurança contra</p>
                    <p>danos a bicicleta.</p>
                </div>
                <div className='block'>
                    <img className="icon4" src={icon4} alt="Reboque"></img>
                    <h3>REBOQUE</h3> 
                    <p className='up'>Segurança em qualquer</p>
                    <p>Lugar</p>
                </div>
            </div>
            <div className='down'><p>Entre outros</p></div>
        </div>
    );
};

export default Assistencia;