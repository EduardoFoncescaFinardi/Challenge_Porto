package br.com.challange.model;

public class Material {

    private String plastico;

    private String fibraDeCarbono;


    public Material() {
    }

    public Material(String plastico, String fibraDeCarbono) {
        this.plastico = plastico;
        this.fibraDeCarbono = fibraDeCarbono;
    }

    public String getPlastico() {
        return plastico;
    }

    public void setPlastico(String plastico) {
        this.plastico = plastico;
    }

    public String getFibraDeCarbono() {
        return fibraDeCarbono;
    }

    public void setFibraDeCarbono(String fibraDeCarbono) {
        this.fibraDeCarbono = fibraDeCarbono;
    }
}


