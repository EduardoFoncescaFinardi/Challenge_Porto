package br.com.domain.entity;

public class Guidao {

    private String marca;

    private String manoplas;

    private String maneteDefreio;

    private String alavancaDeFreio;

    public Guidao() {
    }

    public Guidao(String marca, String manoplas, String maneteDefreio, String alavancaDeFreio) {
        this.setMarca(marca);
        this.setManoplas(manoplas);
        this.setManeteDefreio(maneteDefreio);
        this.setAlavancaDeFreio(alavancaDeFreio);
    }


    public String getMarca() {
        return marca;
    }

    public Guidao setMarca(String marca) {
        this.marca = marca;
        return this;
    }

    public String getManoplas() {
        return manoplas;
    }

    public Guidao setManoplas(String manoplas) {
        this.manoplas = manoplas;
        return this;
    }

    public String getManeteDefreio() {
        return maneteDefreio;
    }

    public Guidao setManeteDefreio(String maneteDefreio) {
        this.maneteDefreio = maneteDefreio;
        return this;
    }

    public String getAlavancaDeFreio() {
        return alavancaDeFreio;
    }

    public Guidao setAlavancaDeFreio(String alavancaDeFreio) {
        this.alavancaDeFreio = alavancaDeFreio;
        return this;
    }

    @Override
    public String toString() {
        return "Guidao{" +
                "marca='" + marca + '\'' +
                ", manoplas='" + manoplas + '\'' +
                ", maneteDefreio='" + maneteDefreio + '\'' +
                ", alavancaDeFreio='" + alavancaDeFreio + '\'' +
                '}';
    }
}
