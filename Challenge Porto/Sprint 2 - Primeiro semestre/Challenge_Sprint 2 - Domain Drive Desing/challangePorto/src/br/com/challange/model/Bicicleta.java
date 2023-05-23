package br.com.challange.model;

public class Bicicleta {


    private String nome;



    private int aro;

    private String material;

    private boolean pedais;

    private String Pneus;

    private String quadro;

    private int marcha;

    private boolean suspensao;

    private String guidao;

    public Bicicleta() {
    }

    public Bicicleta(int aro, String material, boolean pedais, String pneus, String quadro, int marcha, boolean suspensao, String guidao) {
        this.aro = aro;
        this.material = material;
        this.pedais = pedais;
        Pneus = pneus;
        this.quadro = quadro;
        this.marcha = marcha;
        this.suspensao = suspensao;
        this.guidao = guidao;
    }

    public Bicicleta(String nomeBicicleta) {

    }

    public Bicicleta(String tipoMaterial, String tipoGuidao, String tipoAro, String tipoPneus, String tipoQuadro, String tipoMarcha, String tipoSuspensao) {
    }

    public int getAro() {
        return aro;
    }

    public void setAro(int aro) {
        this.aro = aro;
    }

    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public boolean isPedais() {
        return pedais;
    }

    public void setPedais(boolean pedais) {
        this.pedais = pedais;
    }

    public String getPneus() {
        return Pneus;
    }

    public void setPneus(String pneus) {
        Pneus = pneus;
    }

    public String getQuadro() {
        return quadro;
    }

    public void setQuadro(String quadro) {
        this.quadro = quadro;
    }

    public int getMarcha() {
        return marcha;
    }

    public void setMarcha(int marcha) {
        this.marcha = marcha;
    }

    public boolean isSuspensao() {
        return suspensao;
    }

    public void setSuspensao(boolean suspensao) {
        this.suspensao = suspensao;
    }

    public String getGuidao() {
        return guidao;
    }

    public void setGuidao(String guidao) {
        this.guidao = guidao;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

}
