package br.com.challange.model;

public class Quadro {

    private String grande;

    private String pequeno;

    public Quadro() {
    }

    public Quadro(String grande, String pequeno) {
        this.grande = grande;
        this.pequeno = pequeno;
    }

    public String getGrande() {
        return grande;
    }

    public void setGrande(String grande) {
        this.grande = grande;
    }

    public String getPequeno() {
        return pequeno;
    }

    public void setPequeno(String pequeno) {
        this.pequeno = pequeno;
    }
}
