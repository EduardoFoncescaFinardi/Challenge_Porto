package br.com.challange.model;

public class Pneus {

    private String corrida;

    private String chuva;

    private String trilha;


    public Pneus() {
    }

    public Pneus(String corrida, String chuva, String trilha) {
        this.corrida = corrida;
        this.chuva = chuva;
        this.trilha = trilha;
    }

    public String getCorrida() {
        return corrida;
    }

    public void setCorrida(String corrida) {
        this.corrida = corrida;
    }

    public String getChuva() {
        return chuva;
    }

    public void setChuva(String chuva) {
        this.chuva = chuva;
    }

    public String getTrilha() {
        return trilha;
    }

    public void setTrilha(String trilha) {
        this.trilha = trilha;
    }
}
