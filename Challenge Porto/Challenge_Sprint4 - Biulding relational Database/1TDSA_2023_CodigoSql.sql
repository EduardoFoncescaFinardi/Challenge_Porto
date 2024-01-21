DROP TABLE CLIENTE;
DROP TABLE BICICLETA;
DROP TABLE GUIDAO;
DROP TABLE SELIM;
DROP TABLE QUADRO;
DROP TABLE RODAS;

CREATE TABLE CLIENTE(
    ID_CLIENTE INT NOT NULL,
    DT_NASCIMENTO DATE NOT NULL,
    E_MAIL VARCHAR(50) NOT NULL,
    NR_TELEFONE VARCHAR(11) NOT NULL,
    NM_NOME VARCHAR(60) NOT NULL,
    CEP INT NOT NULL,
    CPF VARCHAR(14) NOT NULL UNIQUE,
    CONSTRAINT PK_ID_CLIENTE PRIMARY KEY (ID_CLIENTE)
    );   
    --Crie uma SEQUENCE para cada Tabela
drop sequence seq_CLIENTE;
CREATE SEQUENCE seq_CLIENTE
    start with 1
    increment by 1
    minvalue 1
    maxvalue 1000
    nocycle;
    
    --Crie uma INDEX para cada Tabela;
CREATE INDEX index_CLIENTE ON CLIENTE (NM_NOME);
SELECT * FROM CLIENTE;
DELETE FROM CLIENTE;

CREATE TABLE BICICLETA(
    ID_BICICLETA INT NOT NULL,
    MODELO_DA_BICICLETA VARCHAR(60),
    NOTA_FISCAL FLOAT,
    ID_CLIENTE INT,
    CONSTRAINT pk_id_bicicleta PRIMARY KEY (ID_BICICLETA),
    CONSTRAINT fk_BICICLETA_CLIENTE FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTE(ID_CLIENTE)
   );
   ---
drop sequence seq_BICICLETA;
CREATE SEQUENCE seq_BICICLETA
    start with 1
    increment by 1
    minvalue 1
    maxvalue 100000
    nocycle;
    
   --Crie uma INDEX para cada Tabela;
CREATE INDEX index_BICICLETA ON BICICLETA (NOTA_FISCAL);
SELECT * FROM BICICLETA;
DELETE FROM BICICLETA;

CREATE TABLE GUIDAO(
    ID_GUIDAO INT NOT NULL,
    MARCA_GUIDAO VARCHAR(60),
    MANOPLAS VARCHAR(60),
    MANETE_DE_FREIO VARCHAR(60),
    ALAVANCA_DE_CAMBIO VARCHAR(60) NOT NULL,
    ID_BICICLETA INT NOT NULL,
    CONSTRAINT pk_id_guidao PRIMARY KEY (ID_GUIDAO),
    CONSTRAINT fk_GUIDAO_BICICLETA FOREIGN KEY (ID_BICICLETA) REFERENCES BICICLETA(ID_BICICLETA)
    );
        --Crie uma SEQUENCE para cada Tabela
drop sequence seq_GUIDAO;
CREATE SEQUENCE seq_GUIDAO
    start with 1
    increment by 1
    minvalue 1
    maxvalue 1000
    nocycle;
        --Crie uma INDEX para cada Tabela;
CREATE INDEX index_GUIDAO ON GUIDAO (MANOPLAS);
SELECT * FROM GUIDAO;
DELETE FROM GUIDAO;

CREATE TABLE SELIM(
    ID_SELIM INT NOT NULL,
    MARCA_SELIM VARCHAR(60),
    CANOTE VARCHAR(60),
    MESA VARCHAR(60),
    ABRACADEIRA VARCHAR(60),
    ID_BICICLETA INT NOT NULL,
    CONSTRAINT pk_id_selim PRIMARY KEY (ID_SELIM),
    CONSTRAINT fk_SELIM_BICICLETA FOREIGN KEY (ID_BICICLETA) REFERENCES BICICLETA(ID_BICICLETA)
    );
           --Crie uma SEQUENCE para cada Tabela
drop sequence seq_SELIM;
CREATE SEQUENCE seq_SELIM
    start with 1
    increment by 1
    minvalue 1
    maxvalue 1000
    nocycle;
            --Crie uma INDEX para cada Tabela;
CREATE INDEX index_SELIM ON SELIM (CANOTE);
SELECT * FROM SELIM;
DELETE FROM SELIM;

CREATE TABLE QUADRO(
    ID_QUADRO INT NOT NULL,
    MARCA_QUADRO VARCHAR(60),
    PEDAL VARCHAR(60),
    PEDIVELA VARCHAR(60) NOT NULL,
    CAIXA_DE_DIRECAO VARCHAR(60),
    GARFO VARCHAR(60), 
    ID_BICICLETA INT NOT NULL,
    CONSTRAINT pk_id_quadro PRIMARY KEY (ID_QUADRO),
    CONSTRAINT fk_QUADRO_BICICLETA FOREIGN KEY (ID_BICICLETA) REFERENCES BICICLETA(ID_BICICLETA)
    ); 
              --Crie uma SEQUENCE para cada Tabela
drop sequence seq_QUADRO;
CREATE SEQUENCE seq_QUADRO
    start with 1
    increment by 1
    minvalue 1
    maxvalue 1000
    nocycle;
                --Crie uma INDEX para cada Tabela;
CREATE INDEX index_QUADRO ON QUADRO (PEDAL);
SELECT * FROM QUADRO;
DELETE FROM QUADRO;

CREATE TABLE RODAS(
    ID_RODAS INT NOT NULL,
    MARCA_RODAS VARCHAR(60),
    FREIO VARCHAR(60),
    CAMBIO_TRASEIRO VARCHAR(60) NOT NULL,
    CAMBIO_DIANTEIRO VARCHAR(60) NOT NULL,
    CASSETE VARCHAR(60) NOT NULL,
    CORRENTE VARCHAR(60),
    SUSPENSAO_TRASEIRA VARCHAR(60),
    ID_BICICLETA INT NOT NULL,
    CONSTRAINT pk_id_rodas PRIMARY KEY (ID_RODAS),
    CONSTRAINT fk_RODAS_BICICLETA FOREIGN KEY (ID_BICICLETA) REFERENCES BICICLETA(ID_BICICLETA)
    );
                 --Crie uma SEQUENCE para cada Tabela
drop sequence seq_RODAS;
CREATE SEQUENCE seq_RODAS
    start with 1
    increment by 1
    minvalue 1
    maxvalue 1000
    nocycle;
                    --Crie uma INDEX para cada Tabela;
CREATE INDEX index_RODAS ON RODAS (FREIO);
SELECT * FROM RODAS;
DELETE FROM RODAS;

DECLARE
   cliente_id NUMBER;
BEGIN
   -- Inserção na Tabela CLIENTE
   INSERT INTO CLIENTE (ID_CLIENTE, DT_NASCIMENTO, E_MAIL, NR_TELEFONE, NM_NOME, CEP, CPF) VALUES (seq_CLIENTE.nextval, TO_DATE('12/03/2005', 'DD/MM/YYYY'),'jaofs12.03@gmail.com', '11984399932', 'joao', '08040460', '645375386');
   INSERT INTO CLIENTE (ID_CLIENTE, DT_NASCIMENTO, E_MAIL, NR_TELEFONE, NM_NOME, CEP, CPF) Values (seq_CLIENTE.nextval, TO_DATE('13/02/2001', 'DD/MM/YYYY'),'blats12.03@gmail.com','1198935932','felipe','0365860','690775386');
   INSERT INTO CLIENTE (ID_CLIENTE, DT_NASCIMENTO, E_MAIL, NR_TELEFONE, NM_NOME, CEP, CPF) Values (seq_CLIENTE.nextval, TO_DATE('11/08/2002', 'DD/MM/YYYY'),'edulats12.03@gmail.com','1197605932','eduardo','09031260','01475386');
   INSERT INTO CLIENTE (ID_CLIENTE, DT_NASCIMENTO, E_MAIL, NR_TELEFONE, NM_NOME, CEP, CPF) Values (seq_CLIENTE.nextval, TO_DATE('09/07/2003', 'DD/MM/YYYY'),'miguel12.03@gmail.com','11960305932','miguel','08732260','2215386');
   INSERT INTO CLIENTE (ID_CLIENTE, DT_NASCIMENTO, E_MAIL, NR_TELEFONE, NM_NOME, CEP, CPF) Values (seq_CLIENTE.nextval, TO_DATE('15/06/1997', 'DD/MM/YYYY'),'murilaol12.03@gmail.com','1190405932','murilo','08532332','2798467348');
   INSERT INTO CLIENTE (ID_CLIENTE, DT_NASCIMENTO, E_MAIL, NR_TELEFONE, NM_NOME, CEP, CPF) Values (seq_CLIENTE.nextval, TO_DATE('10/04/1999', 'DD/MM/YYYY'),'lucaoll12.03@gmail.com','11933405932','lucas','08738630','2073624878');
   INSERT INTO CLIENTE (ID_CLIENTE, DT_NASCIMENTO, E_MAIL, NR_TELEFONE, NM_NOME, CEP, CPF) Values (seq_CLIENTE.nextval, TO_DATE('02/02/1992', 'DD/MM/YYYY'),'fredericol12.03@gmail.com','1197653932','frederico','08756632','2002363');


   -- Obtendo o valor atual da sequência seq_CLIENTE
   SELECT seq_CLIENTE.currval INTO cliente_id FROM DUAL;

   -- Início do bloco PL/SQL aninhado
   DECLARE
      id_bicicleta NUMBER;
   BEGIN
      -- Inserções nas tabelas BICICLETA, GUIDAO, SELIM, QUADRO, RODAS

      INSERT INTO BICICLETA (ID_BICICLETA, MODELO_DA_BICICLETA, NOTA_FISCAL, ID_CLIENTE) VALUES (seq_BICICLETA.nextval, 'caloi2022', 1500.50, cliente_id);
      INSERT INTO BICICLETA (ID_BICICLETA, MODELO_DA_BICICLETA, NOTA_FISCAL, ID_CLIENTE) VALUES (seq_BICICLETA.nextval ,'caloi2022', 1500.50, cliente_id);
      insert into BICICLETA (ID_BICICLETA, MODELO_DA_BICICLETA, NOTA_FISCAL, ID_CLIENTE) VALUES (seq_BICICLETA.nextval ,'oggispeed', 1000.20, cliente_id);
      insert into BICICLETA (ID_BICICLETA, MODELO_DA_BICICLETA, NOTA_FISCAL, ID_CLIENTE) VALUES (seq_BICICLETA.nextval ,'sensetracker', 1100.10, cliente_id);
      insert into BICICLETA (ID_BICICLETA, MODELO_DA_BICICLETA, NOTA_FISCAL, ID_CLIENTE) VALUES (seq_BICICLETA.nextval ,'oggi2012', 1300.12, cliente_id);
      insert into BICICLETA (ID_BICICLETA, MODELO_DA_BICICLETA, NOTA_FISCAL, ID_CLIENTE) VALUES (seq_BICICLETA.nextval ,'caloi2013', 1250.11, cliente_id);
      insert into BICICLETA (ID_BICICLETA, MODELO_DA_BICICLETA, NOTA_FISCAL, ID_CLIENTE) VALUES (seq_BICICLETA.nextval ,'caloi2011', 1250.11, cliente_id);
      -- Inserções GUIDAO
      INSERT INTO GUIDAO (ID_GUIDAO, MARCA_GUIDAO, MANOPLAS, MANETE_DE_FREIO, ALAVANCA_DE_CAMBIO, ID_BICICLETA) VALUES (seq_GUIDAO.nextval, 'mtb', 'manopladeborrachamtb', 'maneteshipanotp', 'alavancax-TimeTr', seq_BICICLETA.currval);
      INSERT INTO GUIDAO (ID_GUIDAO, MARCA_GUIDAO, MANOPLAS, MANETE_DE_FREIO, ALAVANCA_DE_CAMBIO, ID_BICICLETA) VALUES (seq_GUIDAO.nextval,'absolute','manoplaDeFerro','maneteGTA','alavancaGTS3X', seq_BICICLETA.currval);
      INSERT INTO GUIDAO (ID_GUIDAO, MARCA_GUIDAO, MANOPLAS, MANETE_DE_FREIO, ALAVANCA_DE_CAMBIO, ID_BICICLETA) VALUES (seq_GUIDAO.nextval,'alfameq','manoplaGTSBorracha','maneteTrial', 'lavancaPaco', seq_BICICLETA.currval);
      INSERT INTO GUIDAO (ID_GUIDAO, MARCA_GUIDAO, MANOPLAS, MANETE_DE_FREIO, ALAVANCA_DE_CAMBIO, ID_BICICLETA) VALUES (seq_GUIDAO.nextval,'avance','manoplaAbsoluteNBR','maneteLogan','alavancaGTA',seq_BICICLETA.currval);  
      INSERT INTO GUIDAO (ID_GUIDAO, MARCA_GUIDAO, MANOPLAS, MANETE_DE_FREIO, ALAVANCA_DE_CAMBIO, ID_BICICLETA) VALUES (seq_GUIDAO.nextval,'Calypso','manoplaBefit','maneteCicloHouse', 'alavancaShimano', seq_BICICLETA.currval);
      INSERT INTO GUIDAO (ID_GUIDAO, MARCA_GUIDAO, MANOPLAS, MANETE_DE_FREIO, ALAVANCA_DE_CAMBIO, ID_BICICLETA) VALUES (seq_GUIDAO.nextval,'Caicara','manoplaJWS','maneteTSW','alavancaPeak',seq_BICICLETA.currval);
      INSERT INTO GUIDAO (ID_GUIDAO, MARCA_GUIDAO, MANOPLAS, MANETE_DE_FREIO, ALAVANCA_DE_CAMBIO, ID_BICICLETA) VALUES (seq_GUIDAO.nextval,'AOLIXIN','manoplaTMBYX','maneteIsapa','alavancaMagideal',seq_BICICLETA.currval);
      -- Inserções Selim
      INSERT INTO SELIM (ID_SELIM, MARCA_SELIM, CANOTE, MESA, ABRACADEIRA, ID_BICICLETA) VALUES (seq_SELIM.nextval, 'selimpowercomp', 'canotedeselimAbsolute', 'mesaMTB', 'abracadeiraAllen', seq_BICICLETA.currval);
      INSERT INTO SELIM (ID_SELIM, MARCA_SELIM, CANOTE, MESA, ABRACADEIRA, ID_BICICLETA) VALUES (seq_SELIM.nextval, 'selimMTB','canotedeselimGTA','mesaAbsolute', 'abracadeiraAbsolute', seq_BICICLETA.currval);
      INSERT INTO SELIM (ID_SELIM, MARCA_SELIM, CANOTE, MESA, ABRACADEIRA, ID_BICICLETA) VALUES (seq_SELIM.nextval,'selimAifeit','canotedeselimGTS','mesaPromax','abracadeiraMuqzi',seq_BICICLETA.currval);
      INSERT INTO SELIM (ID_SELIM, MARCA_SELIM, CANOTE, MESA, ABRACADEIRA, ID_BICICLETA) VALUES (seq_SELIM.nextval,'selimGios','canotedeselimWild','mesaFmfxtr', 'abracadeiraNeroi',seq_BICICLETA.currval);
      INSERT INTO SELIM (ID_SELIM, MARCA_SELIM, CANOTE, MESA, ABRACADEIRA, ID_BICICLETA) VALUES (seq_SELIM.nextval, 'selimLtx','canotedeselimGlossy','mesaUno','abracadeiraAloyy',seq_BICICLETA.currval);
      INSERT INTO SELIM (ID_SELIM, MARCA_SELIM, CANOTE, MESA, ABRACADEIRA, ID_BICICLETA) VALUES (seq_SELIM.nextval, 'selimGta','canotedeselimSenTec','mesaBrave','abracadeiraToken',seq_BICICLETA.currval);
        -- Inserções Quadros
      INSERT INTO QUADRO (ID_QUADRO, MARCA_QUADRO, PEDAL, PEDIVELA, CAIXA_DE_DIRECAO, GARFO, ID_BICICLETA) VALUES (seq_QUADRO.nextval, 'quadroPowercomp', 'pedalShimano', 'pedivelaGTS', 'caixaDeDirecaoAllen', 'garfoDeFerro', seq_BICICLETA.currval);
      INSERT INTO QUADRO (ID_QUADRO, MARCA_QUADRO, PEDAL, PEDIVELA, CAIXA_DE_DIRECAO, GARFO, ID_BICICLETA) VALUES (seq_QUADRO.nextval,'quadroAbsolute','pedalVenzo','pedivelaGTA','aixaDeDirecaoAbsolute', 'garfoAbsolute',seq_BICICLETA.currval);
      INSERT INTO QUADRO (ID_QUADRO, MARCA_QUADRO, PEDAL, PEDIVELA, CAIXA_DE_DIRECAO, GARFO, ID_BICICLETA) VALUES (seq_QUADRO.nextval,'quadroGTI','pedalWelgo','pedivelaIXF','caixaDeDirecaoNeco', 'garfoAllen',seq_BICICLETA.currval);
      INSERT INTO QUADRO (ID_QUADRO, MARCA_QUADRO, PEDAL, PEDIVELA, CAIXA_DE_DIRECAO, GARFO, ID_BICICLETA) VALUES (seq_QUADRO.nextval,'quadroGios','pedalRoyal','pedivelaShimano','caixaDeDirecaoCly','garfoAlloy' ,seq_BICICLETA.currval);
      INSERT INTO QUADRO (ID_QUADRO, MARCA_QUADRO, PEDAL, PEDIVELA, CAIXA_DE_DIRECAO, GARFO, ID_BICICLETA) VALUES (seq_QUADRO.nextval,'quadroGantech','pedalCiclo','pedivelaSugino','caixaDeDirecaoPaco','garfoGTS' ,seq_BICICLETA.currval);
      INSERT INTO QUADRO (ID_QUADRO, MARCA_QUADRO, PEDAL, PEDIVELA, CAIXA_DE_DIRECAO, GARFO, ID_BICICLETA) VALUES (seq_QUADRO.nextval,'quadroForss','pedalMetal','pedivelaGTS','caixaDeDirecaoMega','garfoPaco', seq_BICICLETA.currval);
      INSERT INTO QUADRO (ID_QUADRO, MARCA_QUADRO, PEDAL, PEDIVELA, CAIXA_DE_DIRECAO, GARFO, ID_BICICLETA) VALUES (seq_QUADRO.nextval,'quadroKylin','pedalCrank','pedivelaCross','caixaDeDirecaoYamada','garfoShimano' ,seq_BICICLETA.currval);
      -- Inserções Rodas
      INSERT INTO RODAS (ID_RODAS, MARCA_RODAS, FREIO, CAMBIO_TRASEIRO, CAMBIO_DIANTEIRO, CASSETE, CORRENTE, SUSPENSAO_TRASEIRA, ID_BICICLETA) VALUES (seq_RODAS.nextval, 'rodasAbsolute', 'freioShimano', 'cambioTraseiroAbsolute', 'cambioDianteiroAllen', 'casseteMtb', 'correnteTec', 'suspencaoTraseiraDnm', seq_BICICLETA.currval);
      insert into RODAS (ID_RODAS, MARCA_RODAS, FREIO, CAMBIO_TRASEIRO, CAMBIO_DIANTEIRO, CASSETE, CORRENTE, SUSPENSAO_TRASEIRA, ID_BICICLETA) VALUES (seq_RODAS.nextval,'rodasDt','freioTrekt','cambioTraseiroShimano','cambioDianteiroShimano','casseteShimano','correnteXtec', 'suspencaoTraseiraZomm' , seq_BICICLETA.currval);
      insert into RODAS (ID_RODAS, MARCA_RODAS, FREIO, CAMBIO_TRASEIRO, CAMBIO_DIANTEIRO, CASSETE, CORRENTE, SUSPENSAO_TRASEIRA, ID_BICICLETA) VALUES (seq_RODAS.nextval,'rodasSentec','freioJagwire','cambioTraseiroSun','cambioDianteiroSun','casseteZtto','correnteAlloy', 'suspencaoTraseiraMode' ,seq_BICICLETA.currval);
      insert into RODAS (ID_RODAS, MARCA_RODAS, FREIO, CAMBIO_TRASEIRO, CAMBIO_DIANTEIRO, CASSETE, CORRENTE, SUSPENSAO_TRASEIRA, ID_BICICLETA) VALUES (seq_RODAS.nextval,'rodasVzan','freioHigh','cambioTraseiroRace','cambioDianteiroRace','casseteRace','correnteGx', 'suspencaoTraseiraGx' ,seq_BICICLETA.currval);
      insert into RODAS (ID_RODAS, MARCA_RODAS, FREIO, CAMBIO_TRASEIRO, CAMBIO_DIANTEIRO, CASSETE, CORRENTE, SUSPENSAO_TRASEIRA, ID_BICICLETA) VALUES (seq_RODAS.nextval,'rodasKfb','freioOne','cambioTraseiroWg','cambioDianteiroWg','casseteEagle','correnteEagle', 'suspencaoTraseiraSuntour' ,seq_BICICLETA.currval);
      insert into RODAS (ID_RODAS, MARCA_RODAS, FREIO, CAMBIO_TRASEIRO, CAMBIO_DIANTEIRO, CASSETE, CORRENTE, SUSPENSAO_TRASEIRA, ID_BICICLETA) VALUES (seq_RODAS.nextval,'rodasAlexin','freioAligattor','cambioTraseiroSram','cambioDianteiroAltus','casseteSun','correnteCrom', 'suspencaoTraseiraShock' ,seq_BICICLETA.currval);
      insert into RODAS (ID_RODAS, MARCA_RODAS, FREIO, CAMBIO_TRASEIRO, CAMBIO_DIANTEIRO, CASSETE, CORRENTE, SUSPENSAO_TRASEIRA, ID_BICICLETA) VALUES (seq_RODAS.nextval,'rodasShimano','freioAbsolute','cambioTraseiroTiagra','cambioDianteiroSora','casseteSunRun','correnteElos', 'suspencaoTraseiraAbsolute' ,seq_BICICLETA.currval);

      -- Obtendo o valor atual da sequência seq_BICICLETA
      SELECT seq_BICICLETA.currval INTO id_bicicleta FROM DUAL;


   END; -- Fim do bloco PL/SQL aninhado

   -- Restante do bloco externo, se houver

END;
/

-- Relatorios--
-- Relatório ordenando dados da tabela SELIM por MARCA_SELIM
SELECT
    MARCA_SELIM,
    CANOTE,
    MESA,
    ABRACADEIRA,
    ID_BICICLETA
FROM
    SELIM
ORDER BY
    MARCA_SELIM;
-- Calcular a média da nota fiscal das bicicletas
SELECT AVG(NOTA_FISCAL) AS MEDIA_NOTA_FISCAL
FROM BICICLETA;
-- Calcular a média da nota fiscal das bicicletas por marca de guidão
SELECT
    G.MARCA_GUIDAO,
    AVG(B.NOTA_FISCAL) AS MEDIA_NOTA_FISCAL
FROM
    GUIDAO G
JOIN
    BICICLETA B ON G.ID_BICICLETA = B.ID_BICICLETA
GROUP BY
    G.MARCA_GUIDAO;
-- Encontrar bicicletas com a menor nota fiscal e os detalhes do cliente
SELECT
    B.ID_BICICLETA,
    B.NOTA_FISCAL,
    C.NM_NOME
FROM
    BICICLETA B
JOIN
    CLIENTE C ON B.ID_CLIENTE = C.ID_CLIENTE
WHERE
    B.NOTA_FISCAL = (
        SELECT MIN(NOTA_FISCAL) FROM BICICLETA
    );
-- Relatório com junção de tabelas para mostrar detalhes do cliente e da bicicleta
SELECT
    C.NM_NOME AS NOME_CLIENTE,
    B.ID_BICICLETA,
    B.NOTA_FISCAL
FROM
    CLIENTE C
JOIN
    BICICLETA B ON C.ID_CLIENTE = B.ID_CLIENTE;


--?	Eduardo Finardi | RM: 98624
--?	Miguel Santos | RM: 551640
--?	Murilo Munari | RM: 94164
--?	Felipe Morais | RM: 551463
--?	João Cardoso | RM: 552078
