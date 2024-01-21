import React, { useState } from 'react';
import './Plano.css';
import biketravel from '../../images/biketravel.png';
import { Link } from "react-router-dom";

const Plano = () => {
    const [descricao, setDescricao] = useState({
        elite: false,
        medio: false,
        normal: false,
    });

    const handleCheckboxChange = (plano) => {
        setDescricao({ ...descricao, [plano]: !descricao[plano] });
    };

    return (
        <div className='planos'>
            <section className='img-bike'>
                <img className="biketravel" src={biketravel} alt="bike-travel"></img>
            </section>
            <section className='container-planos'>
                <div className='container-box'>
                    <input
                        type='checkbox'
                        className='checkbox'
                        checked={descricao.elite}
                        onChange={() => handleCheckboxChange('elite')}
                    />
                    <label>Plano Elite</label>
                </div>
                <div className={`descricao ${descricao.elite ? 'show' : ''}`}>
                    <p className='descricao-text'>
                        <li>Quebra acidental</li>
                        <li>Roubo</li>
                        <li>Furto Qualificado</li>
                        <li>Sem carência</li>
                        <li>100% online</li>
                        <li>Assistência 24h ilimitada</li>
                    </p>
                </div>

                <div className='container-box'>
                    <input
                        type='checkbox'
                        className='checkbox'
                        checked={descricao.medio}
                        onChange={() => handleCheckboxChange('medio')}
                    />
                    <label>Plano Médio</label>
                </div>
                <div className={`descricao ${descricao.medio ? 'show' : ''}`}>
                    <p className='descricao-text'>
                        <li>Quebra acidental</li>
                        <li>Roubo</li>
                        <li>Furto Qualificado</li>
                        <li>Sem carência</li>
                        <li>100% online</li>
                        <li>Assistência 24h</li>
                    </p>
                </div>

                <div className='container-box'>
                    <input
                        type='checkbox'
                        className='checkbox'
                        checked={descricao.normal}
                        onChange={() => handleCheckboxChange('normal')}
                    />
                    <label>Plano Normal</label>
                </div>
                <div className={`descricao ${descricao.normal ? 'show' : ''}`}>
                    <p className='descricao-text'>
                        <li>Roubo</li>
                        <li>Furto Qualificado</li>
                        <li>Sem carência</li>
                        <li>100% online</li>
                    </p>
                </div>
                <>
                <Link to="/Cotacao"><button className='box-action'>Cotação</button></Link>
                </>
            </section>
        </div>
    );
};

export default Plano;