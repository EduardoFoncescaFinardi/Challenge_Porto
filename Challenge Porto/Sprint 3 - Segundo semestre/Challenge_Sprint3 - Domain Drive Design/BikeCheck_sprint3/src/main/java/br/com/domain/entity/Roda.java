package br.com.domain.entity;

public class Roda {

    private String marca;

    private String freio;

    private String cambioTraseiro;

    private String cambioDianteiro;

    private String cassete;

    private String corrente;

    private String suspensao;

    public Roda() {
    }

    public Roda(String marca, String freio, String cambioTraseiro, String cambioDianteiro, String cassete, String corrente, String suspensao) {
        this.setMarca(marca);
        this.setFreio(freio);
        this.setCambioTraseiro(cambioTraseiro);
        this.setCambioDianteiro(cambioDianteiro);
        this.setCassete(cassete);
        this.setCorrente(corrente);
        this.setSuspensao(suspensao);
    }

    public String getMarca() {
        return marca;
    }

    public Roda setMarca(String marca) {
        this.marca = marca;
        return this;
    }

    public String getFreio() {
        return freio;
    }

    public Roda setFreio(String freio) {
        this.freio = freio;
        return this;
    }

    public String getCambioTraseiro() {
        return cambioTraseiro;
    }

    public Roda setCambioTraseiro(String cambioTraseiro) {
        this.cambioTraseiro = cambioTraseiro;
        return this;
    }

    public String getCambioDianteiro() {
        return cambioDianteiro;
    }

    public Roda setCambioDianteiro(String cambioDianteiro) {
        this.cambioDianteiro = cambioDianteiro;
        return this;
    }

    public String getCassete() {
        return cassete;
    }

    public Roda setCassete(String cassete) {
        this.cassete = cassete;
        return this;
    }

    public String getCorrente() {
        return corrente;
    }

    public Roda setCorrente(String corrente) {
        this.corrente = corrente;
        return this;
    }

    public String getSuspensao() {
        return suspensao;
    }

    public Roda setSuspensao(String suspensao) {
        this.suspensao = suspensao;
        return this;
    }

    @Override
    public String toString() {
        return "Roda{" +
                "marca='" + marca + '\'' +
                ", freio='" + freio + '\'' +
                ", cambioTraseiro='" + cambioTraseiro + '\'' +
                ", cambioDianteiro='" + cambioDianteiro + '\'' +
                ", cassete='" + cassete + '\'' +
                ", corrente='" + corrente + '\'' +
                ", suspensao='" + suspensao + '\'' +
                '}';
    }
}
