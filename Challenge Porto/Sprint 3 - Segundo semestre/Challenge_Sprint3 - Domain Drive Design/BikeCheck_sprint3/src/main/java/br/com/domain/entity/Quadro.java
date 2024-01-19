package br.com.domain.entity;

public class Quadro {

    private String marca;

    private String pedal;

    private String pedivela;

    private String caixaDirecao;

    private String garfo;

    public Quadro() {
    }

    public Quadro(String marca, String pedal, String pedivela, String caixaDirecao, String garfo) {
        this.setMarca(marca);
        this.setPedal(pedal);
        this.setPedivela(pedivela);
        this.setCaixaDirecao(caixaDirecao);
        this.setGarfo(garfo);
    }


    public String getMarca() {
        return marca;
    }

    public Quadro setMarca(String marca) {
        this.marca = marca;
        return this;
    }

    public String getPedal() {
        return pedal;
    }

    public Quadro setPedal(String pedal) {
        this.pedal = pedal;
        return this;
    }

    public String getPedivela() {
        return pedivela;
    }

    public Quadro setPedivela(String pedivela) {
        this.pedivela = pedivela;
        return this;
    }

    public String getCaixaDirecao() {
        return caixaDirecao;
    }

    public Quadro setCaixaDirecao(String caixaDirecao) {
        this.caixaDirecao = caixaDirecao;
        return this;
    }

    public String getGarfo() {
        return garfo;
    }

    public Quadro setGarfo(String garfo) {
        this.garfo = garfo;
        return this;
    }

    @Override
    public String toString() {
        return "Quadro{" +
                "marca='" + marca + '\'' +
                ", pedal='" + pedal + '\'' +
                ", pedivela='" + pedivela + '\'' +
                ", caixaDirecao='" + caixaDirecao + '\'' +
                ", garfo='" + garfo + '\'' +
                '}';
    }
}
