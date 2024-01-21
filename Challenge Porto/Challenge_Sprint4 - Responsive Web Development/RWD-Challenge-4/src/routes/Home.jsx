import React from "react";
import Bannerimg from '../components/Banner/Banner'
import AssisteciaContainer from '../components/Assistencias/Assistencia'
import DuvidasSumarry from '../components/Duvidas/Duvidas'
import Linha from '../components/Linha/Linha'
import Planos from '../components/Planos/Plano'

const Home = () => {
    return(
        <div>
            <Bannerimg/>
            <AssisteciaContainer/>
            <Linha/>
            <Planos/>
            <Linha/>
            <DuvidasSumarry/>
            <Linha/>
        </div>
    );
};

export default Home;