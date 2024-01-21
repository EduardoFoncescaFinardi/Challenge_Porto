import './Duvidas.css'
import { FcCollapse } from "react-icons/fc";

const Duvidas = () => {

    return(
        <div className='duvidas'>
            <h3>Dúvidas Frequentes</h3>
            <section>
                <details>
                    <summary className='sumarry' ><FcCollapse style = {{transform: 'rotate(90deg)'}}/>O seguro cobre acessórios?</summary>
                    <p> Sim, o seguro cobre acessórios!</p>
                </details>
                <details>
                    <summary className='sumarry'><FcCollapse style = {{transform: 'rotate(90deg)' }}/>Não tenho nota fiscal, posso contratar o seguro?</summary>
                    <p> Pode. Porem vale ressaltar que podemos solicitar comprovações da existência e posse do bem.</p>
                </details>
                <details>
                    <summary className='sumarry'><FcCollapse style = {{transform: 'rotate(90deg)' }}/>O Seguro cobre furto simples?</summary>
                    <p> Não, a cobertura só é acionada mediante o emprego de violência ou o rompimento de obstáculos do local, desde que existam provas.</p>
                </details>
                <details>
                    <summary className='sumarry'><FcCollapse style = {{transform: 'rotate(90deg)' }}/>Vocês aceitam bikes personalizadas?</summary>
                    <p> Sim, aceitamos bicicletas que tiverem seus componentes alterados ou personalizadas, desde que em eventual sinistro, tenha comprovação da aquisição de todos os componentes. Sempre que houver uma nova alteração de peças que altere o valor total da bicicleta, deverá ser feita uma nova vistoria.</p>
                </details>
                <details>
                    <summary className='sumarry'><FcCollapse style = {{transform: 'rotate(90deg)' }}/>Preciso estar com a bike em mãos para contratar o seguro?</summary>
                    <p>Sim, porém para finalizar a contratação do seguro, precisará estar com a bike em mãos para mandar fotos.</p>
                </details>
            </section>
        </div>
    );
};

export default Duvidas;