package br.com.domain.view;

import br.com.domain.entity.*;
import br.com.domain.repository.BicicletaRepository;
import br.com.domain.service.ClienteService;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class MenuView {

    List<Bicicleta> bicicletas = new ArrayList<>();
    private ClienteService service = new ClienteService();

    public static void main(String[] args) {
        MenuView menuView = new MenuView();
        menuView.menu();
    }

    public void menu() {
        int escolha = 0;

        do {
            escolha = Integer.parseInt(JOptionPane.showInputDialog("Escolha uma opção: \n" +
                    "1 - Adicionar Cliente \n" +
                    "2 - Encerrar programa"));

            if (escolha == 1) {
                Cliente cliente = addCliente();
                if (cliente != null) {
                    System.out.println("Cliente criado:\n" + cliente);
                    informarPecasBicicleta(cliente);
                }
            } else if (escolha == 2) {
                System.out.println("Encerrando o programa.");
                System.exit(0);
            }
        } while (escolha != 2);
    }

    public Cliente addCliente() {
        Cliente cliente = new Cliente();

        String usuario = JOptionPane.showInputDialog("Digite o nome de usuário:");
        if (usuario == null || usuario.isEmpty()) {
            System.out.println("Usuário inválido.");
            return null;
        }
        cliente.setUsuario(usuario);

        String senha = JOptionPane.showInputDialog("Digite a senha:");
        if (senha == null || senha.isEmpty()) {
            System.out.println("Senha inválida.");
            return null;
        }
        cliente.setSenha(senha);

        BicicletaRepository bicicletaRepository = new BicicletaRepository();
        bicicletas = bicicletaRepository.findAll();

        if (bicicletas.size() > 0) {
            Bicicleta bicicletaEscolhida = escolherBicicleta(bicicletas);

            if (bicicletaEscolhida == null) {
                System.out.println("Cliente não foi criado.");
                return null;
            }

            cliente.addBicicleta(String.valueOf(bicicletaEscolhida));

            Cliente persist = service.persist(cliente);

            if (persist != null) {
                System.out.println("Cliente criado com sucesso!");
                return persist;
            } else {
                System.out.println("Cliente não foi criado.");
            }
        }
        return null;
    }

    private Bicicleta escolherBicicleta(List<Bicicleta> bicicletas) {
        Object[] bicicletasArray = bicicletas.toArray();
        Bicicleta bicicletaEscolhida = (Bicicleta) JOptionPane.showInputDialog(
                null, "Escolha a bicicleta", "Tipos de bicicleta",
                JOptionPane.QUESTION_MESSAGE, null, bicicletasArray, bicicletasArray[0]);

        return bicicletaEscolhida;
    }


    private void informarPecasBicicleta(Cliente cliente) {
        List<PecaBicicleta> pecasEscolhidas = new ArrayList<>();

        String[] nomesPecas = {"guidão", "quadro", "selim", "rodas"};
        for (String nomePeca : nomesPecas) {
            String marca = JOptionPane.showInputDialog(null, "Digite a marca do " + nomePeca + ":");

            if (marca == null || marca.isEmpty()) {
                System.out.println("Marca de peça inválida.");
                return;
            }

            PecaBicicleta peca = null;

            // Solicite informações específicas para cada tipo de peça
            Selim selim = new Selim();
            Roda roda = new Roda();
            Quadro quadro = new Quadro();
            Guidao guidao = new Guidao();
            switch (nomePeca) {
                case "guidão":
                    String manoplas = JOptionPane.showInputDialog(null, "Digite as manoplas:");
                    String maneteDeFreio = JOptionPane.showInputDialog(null, "Digite o manete de freio:");
                    String alavancaDeFreio = JOptionPane.showInputDialog(null, "Digite o material  da alavanca de freio:");
                    guidao = new Guidao(marca, manoplas, maneteDeFreio, alavancaDeFreio);
                    break;

                case "quadro":
                    String pedal = JOptionPane.showInputDialog(null, "Digite o material do pedal:");
                    String pedivela = JOptionPane.showInputDialog(null, "Digite o  material pedivela:");
                    String caixaDirecao = JOptionPane.showInputDialog(null, "Digite a caixa de direção:");
                    String garfo = JOptionPane.showInputDialog(null, "Digite o modelo do garfo:");
                    quadro = new Quadro(marca, pedal, pedivela, caixaDirecao, garfo);
                    break;

                case "selim":
                    String canote = JOptionPane.showInputDialog(null, "Digite o material do canote:");
                    String mesa = JOptionPane.showInputDialog(null, "Digite o tamnaho da mesa:");
                    String abracadeira = JOptionPane.showInputDialog(null, "Digite o material da  abraçadeira:");
                    selim = new Selim(marca, canote, mesa, abracadeira);
                    break;

                case "rodas":
                    String marcaFreio = JOptionPane.showInputDialog(null, "Digite o modelo do freio:");
                    String cambioTraseiro = JOptionPane.showInputDialog(null, "Digite o modelo do câmbio traseiro:");
                    String cambioDianteiro = JOptionPane.showInputDialog(null, "Digite o modelo do câmbio dianteiro:");
                    String cassete = JOptionPane.showInputDialog(null, "Digite o modelo cassete:");
                    String corrente = JOptionPane.showInputDialog(null, "Digite o material da corrente:");
                    String suspensao = JOptionPane.showInputDialog(null, "Digite o modelo da suspensão:");
                    roda = new Roda(marca, marcaFreio, cambioTraseiro, cambioDianteiro, cassete, corrente, suspensao);
                    break;

                default:
                    System.out.println("Nome de peça desconhecido: " + nomePeca);
                    return;
            }

            pecasEscolhidas.add(peca);

        }

        cliente.getBicicletas().get(0).setPecas(pecasEscolhidas.toString());

        System.out.println("Peças da bicicleta:");
        for (PecaBicicleta peca : pecasEscolhidas) {
            System.out.println(peca);
        }
        System.out.println("Peças da bicicleta registradas com sucesso!");
    }

}
