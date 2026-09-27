USE helpdesk;
-- População rápida para testes
-- Execute DEPOIS de: alembic upgrade head

-- Limpar tabelas (desabilitando FK temporariamente)
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE tickets;
TRUNCATE TABLE categorias;
TRUNCATE TABLE usuarios;
ALTER TABLE usuarios AUTO_INCREMENT = 1;
ALTER TABLE tickets AUTO_INCREMENT = 1;
ALTER TABLE categorias AUTO_INCREMENT = 1;
SET FOREIGN_KEY_CHECKS = 1;

-- Inserir usuários (admin e atendente)
-- Papel: ADMIN, ATENDENTE, SOLICITANTE (conforme migration 2f4c71811f37)
-- Nota: O enum no código só tem ATENDENTE e SOLICITANTE, use ATENDENTE para o admin
INSERT INTO usuarios (nome, email, senha_hash, papel, ativo, criado_em) VALUES
('Administrador', 'admin@helpdesk.com', '$2b$12$examplehash1', 'ATENDENTE', TRUE, NOW()),
('João Silva', 'joao@helpdesk.com', '$2b$12$examplehash2', 'SOLICITANTE', TRUE, NOW()),
('Maria Oliveira', 'maria@helpdesk.com', '$2b$12$examplehash3', 'ATENDENTE', TRUE, NOW());

-- Inserir categorias
INSERT INTO categorias (nome, descricao, ativa, criado_em) VALUES
('Geral', 'Assuntos gerais do helpdesk', TRUE, NOW()),
('Software', 'Problemas e solicitações de software', TRUE, NOW()),
('Hardware', 'Problemas e solicitações de hardware', TRUE, NOW());

-- Inserir tickets de teste
INSERT INTO tickets (numero_protocolo, titulo, descricao, status, prioridade, setor, descricao_solucao, motivo_cancelamento, data_criacao, data_atualizacao, solicitante_id, atendente_id) VALUES
('PROT-001', 'Sistema lento', 'O sistema está muito lento após atualização', 'ABERTO', 'ALTA', 'TI', NULL, NULL, NOW(), NULL, 2, NULL),
('PROT-002', 'Acesso negado', 'Usuário não pode acessar o modulo financeiro', 'EM_ANALISE', 'MEDIA', 'FINANCEIRO', NULL, NULL, NOW(), NULL, 2, 1),
('PROT-003', 'Impressora não imprime', 'Impressora da sala 102 não está imprimindo', 'RESOLVIDO', 'BAIXA', 'MANUTENCAO', 'Substituída a impressora thermal', NULL, NOW(), NOW(), 2, 1),
('PROT-004', 'Reset de senha', 'Usuário solicitou reset de senha', 'CANCELADO', 'BAIXA', 'ADMINISTRATIVO', NULL, 'Usuário desistiu', NOW(), NULL, 3, NULL),
('PROT-005', 'Acesso a VPN', 'Problema de conexão VPN após mudança de rede', 'ABERTO', 'ALTA', 'TI', NULL, NULL, NOW(), NULL, 3, NULL);