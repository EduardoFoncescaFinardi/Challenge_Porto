package br.com.challange.model;

public class Guidao {

    private String corrida;

    private String passeio;

    public Guidao() {
    }

    public Guidao(String corrida, String passeio) {
        this.corrida = corrida;
        this.passeio = passeio;
    }

    public String getCorrida() {
        return corrida;
    }

    public void setCorrida(String corrida) {
        this.corrida = corrida;
    }

    public String getPasseio() {
        return passeio;
    }

    public void setPasseio(String passeio) {
        this.passeio = passeio;
    }
}
