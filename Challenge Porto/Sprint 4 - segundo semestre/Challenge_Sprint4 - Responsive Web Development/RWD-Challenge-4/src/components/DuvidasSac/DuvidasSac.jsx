import './DuvidasSac.css'
import bikeparking from '../../images/bike-parking.png'


const DuvidasSac = () => {
    return(
        <div className='ds-container'>
            <div className='ds-quest'>
                <div className='ds-perguntas'>
                    <h3>Qual as formas de <span>pagamento</span> do seguro?</h3>
                    <p>Nós aceitamos cartão de credito e debito. </p>
                </div>
                <div className='ds-perguntas'>
                    <h3>Posso <span>contratar</span> seguro para bikes usadas?</h3>
                    <p>Sim, você pode contratar o seguro para bicicletas tradicionais até 8 anos de uso, e bicicletas elétricas com até 3 anos de uso. </p>
                </div>
                <div className='ds-perguntas'>
                    <h3>O seguro oferece cobertura para <span>acessórios?</span></h3>
                    <p>Sim, tem cobertura para acessórios da bike, como por exemplo ciclocomputadores, GPS e velocímetros. </p>
                </div>
                <div className='ds-perguntas'>
                    <h3>É necessário apresentar algum <span>documento</span> para contratar o seguro de bike?</h3>
                    <p>Sim, em caso de sinistro, solicitamos a nota fiscal da bike ou algum documento de comprovação.</p>
                </div>
                <div className='ds-perguntas'>
                    <h3>Como é feita a <span>vistoria</span> da bicicleta?</h3>
                    <p>A  vistoria da bicicleta é bem simples, normalmente as seguradoras solicitam as fotos da bicicleta, o número de série e algumas informações de modificações.</p>
                </div>
            </div>
            <div className='container-img'>
                <div className='bike-parking img'>
                    <img src={bikeparking} alt='Img-parking-bike'></img>
                </div>
            </div>
        </div>
    );
};

export default DuvidasSac;