package br.com.domain.entity;

public class Selim {

    private String marca;

    private String canote;

    private String mesa;

    private String abracadeira;

    public Selim() {
    }

    public Selim(String marca, String canote, String mesa, String abracadeira) {
        this.setMarca(marca);
        this.setCanote(canote);
        this.setMesa(mesa);
        this.setAbracadeira(abracadeira);
    }



    public String getMarca() {
        return marca;
    }

    public Selim setMarca(String marca) {
        this.marca = marca;
        return this;
    }

    public String getCanote() {
        return canote;
    }

    public Selim setCanote(String canote) {
        this.canote = canote;
        return this;
    }

    public String getMesa() {
        return mesa;
    }

    public Selim setMesa(String mesa) {
        this.mesa = mesa;
        return this;
    }

    public String getAbracadeira() {
        return abracadeira;
    }

    public Selim setAbracadeira(String abracadeira) {
        this.abracadeira = abracadeira;
        return this;
    }

    @Override
    public String toString() {
        return "Selim{" +
                "marca='" + marca + '\'' +
                ", canote='" + canote + '\'' +
                ", mesa='" + mesa + '\'' +
                ", abracadeira='" + abracadeira + '\'' +
                '}';
    }
}
