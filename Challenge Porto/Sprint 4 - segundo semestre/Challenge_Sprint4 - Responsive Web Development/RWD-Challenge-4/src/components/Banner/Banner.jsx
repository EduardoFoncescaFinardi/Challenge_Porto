import './Banner.css'
import Bannerimg from '../../images/bannerhdc.png'

const Banner = () => {
    return(
        <div className="img-banner">
            <img src={Bannerimg} alt='Banner Bike'></img>
        </div>
    );
};

export default Banner;