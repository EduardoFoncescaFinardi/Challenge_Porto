import br.com.challange.model.*;
import javax.swing.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Bicicleta bicicleta;

        int encerrar = 0;

        do {
            var nomeBicicleta = JOptionPane.showInputDialog("Bicicleta");

            var tipoMaterial = JOptionPane.showInputDialog("Material");

            var tipoPneus = JOptionPane.showInputDialog("Pneus");

            var tipoAro = JOptionPane.showInputDialog("Aro");

            var tipoQuadro = JOptionPane.showInputDialog("Quadro");

            var tipoMarcha = JOptionPane.showInputDialog("Marcha");

            var tipoSuspensao = JOptionPane.showInputDialog("Suspensão");

            var tipoGuidao = JOptionPane.showInputDialog("Guidão");

            bicicleta = new Bicicleta(tipoMaterial, tipoGuidao, tipoAro, tipoPneus, tipoQuadro, tipoMarcha, tipoSuspensao);

            var pergunta = """
                    Deseja cadastrar mais uma bicicleta?
                    [ 1 ] SIM
                    [ 0 ] NÃO
                    """;
            encerrar = Integer.parseInt(JOptionPane.showInputDialog(pergunta));

        } while (encerrar > 0);

        JOptionPane.showMessageDialog(null, "Bicicleta cadastrada: " + bicicleta);

        System.exit(0);
    }
}
