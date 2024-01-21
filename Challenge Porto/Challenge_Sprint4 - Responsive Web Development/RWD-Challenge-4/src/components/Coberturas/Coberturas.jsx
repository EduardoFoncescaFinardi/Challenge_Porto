import './Coberturas.css'
import { FcInfo } from "react-icons/fc";


const Coberturas = () => {
    return(
        <div className='container-sac'>
            <div className='ti-sac'>
                <h3>Coberturas</h3>
            </div>
            <section className='duvidas-sac'>
                <article>
                    <div className='pgt-sac'><p><FcInfo/> Danos causados por acidentes durante o pedal.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Transporte realizado pelo segurado ou por terceiros.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Cobertura para utilização da bike no exterior.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Acidentes durante a competição.</p></div>
                </article>
                <article>
                    <div className='pgt-sac'><p><FcInfo/> Substituição e regulagem manetes de freios e cabo de aço.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Acidentes pessoais.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Lubrificação de correntes e coroas.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Instalação de suporte de parede e chão para bike.</p></div>
                </article>
                <article>
                    <div className='pgt-sac'><p><FcInfo/> Responsabilidade civil.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Bike Bagagem.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Substituição ou regulagem de freio dianteiro e traseiro.</p></div>
                    <div className='pgt-sac'><p><FcInfo/> Substituição de peças e acessórios em caso de acidentes.</p></div>
                </article>
            </section>
        </div>
    );
};

export default Coberturas;
