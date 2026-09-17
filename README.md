# Centro da Informação de Infraestrutura Universitária
Sistema de denúncias de problemas estruturais da UFRPE				
DESENVOLVEDORES: Festo Murilo, Lucas Manoel e Nicolas Rodrigues.					
				
RF001 - Cadastro/Login	
  FLUXO PRINCIPAL
	1.1-Usuário acessa o site.				
	1.2-Usuário clica em 'fazer cadastro' ( caso já possua prossegue direto para login)				
	1.3-Usuário digita seu nome 				
	1.4-Usuário digita seu email institucional				
	1.5-Código é enviado para email institucional do usuário				
	1.6-Usuário precisa colocar código para confirmar email				
	1.7-Usuário digita e confirma a senha dentro do padrão. Padrão da senha: min 8 caracteres; max 20 caracteres. Deve conter: letras maiusculas, letras minusculas, e números. Opcional: caracteres especiais.				
	1.8-Usuário seleciona curso que está cursando				
	1.9-Cadastro realizado com sucesso				
	2.1-Usuário clica em 'fazer login'				
	2.2-Usuário digita email e senha				
	2.3-Login realizado com sucesso				
	FLUXOS ALTERNATIVOS E DE ERRO				
	1-Email inválido -> Sistema exibe 'E-mail inválido, tente novamente'				
	2-Senha fora do padrão -> Sistema exibe 'Senha fora do padrão'				
	3-Nome de usuário já existe -> Sistema exibe 'Nome de usuário já existente'				
RF002 - Solicitações	----------------------------------------------------------------------------------------------------		-------------------------------------------------------------		-----------------------
	FLUXO PRINCIPAL	
	1.1-Usuário passa pelo login/cadastro.				
	1.2-Usuário acessa a primeira aba onde pode ver todas as solicitações feitas até então.				
	2.1-Usuário se quiser pode selecionar uma das solicitações				
	2.2-Se selecionada uma nova aba é aberta, onde o usuário pode ver mais detalhes da solicitação e participar da enquete.				
	3.1-Usuário se quiser pode criar uma nova solicitção				
	3.2-Caso pretenda criar, uma nova aba é aberta onde a solicitção pode ser feita. Nela deve possuir título, texto informando qual, onde e quando notou que o problema existe. Esses são os requisitos.				
	3.3-Quando o usuário clicar para enviar a solicitação. Ela será enviada para avaliação por nosso sistema. Primeiro será avaliado se a solicitação segue os requisitos. Segundo se ela age contra as diretrizes da UFRPE.	
	3.4-Se a solicitação for aprovada pela moderação, a solicitação será postada no site para visualização dos usuários.				
	3.5-Surge uma mensagem para o usuário que criou a nova solicitação "Obrigado por sua contribuição, a UFRPE agradece".				
	3.6-O usuário retorna à aba inicial				
	4.1-Pode pesquisar categorias de solicitações				
	4.2-Usuário pode sair do CIIU				
	FLUXOS ALTERNATIVOS E DE ERRO				
	1-Requisitos não atendidos-> Sistema exibe "Solicitação incompleta, tente novamente"				
	2-Solicitação viola diretrizes da UFRPE-> Sistema exibe "Esta solicitação viola as diretrizes da UFRPE e será arquivada"				
	----------------------------------------------------------------------------------------------------		--------------------------------------------------------------		-----------------------
RF003 - Feature/Enquente	
  FLUXO PRINCIPAL
	1.1-O sistema cria a tabela de enquete no banco de dados.				
	1.2-O sistema vincula a enquete à denúncia correspondente por meio de uma chave estrangeira.				
	1.3-O usuário acessa a tela da denúncia.				
	1.4-O sistema exibe a enquete disponível para votação.				
	1.5-O sistema verifica se o usuário já votou na enquete.				
	1.6-Caso o usuário ainda não tenha votado, ele seleciona uma das opções disponíveis.				
	1.7-O usuário confirma o voto.				
	1.8-O sistema registra o voto e acrescenta uma unidade ao total da opção selecionada.				
	1.9-O sistema exibe o resultado atualizado da enquete.				
	1.10-A enquete e as demais páginas são apresentadas com a estilização definida para o site.				
	FLUXOS ALTERNATIVOS E DE ERRO				
	1-Usuário já votou na enquete -> Sistema não permite um novo voto e exibe apenas o resultado atual.				
	2-Enquete não vinculada à denúncia -> Sistema não exibe a enquete na tela da denúncia.				
	3-Falha ao registrar o voto -> Sistema exibe "Não foi possível registrar seu voto. Tente novamente".				
	4-Nenhuma opção selecionada -> Sistema exibe "Selecione uma opção antes de confirmar o voto".				
	----------------------------------------------------------------------------------------------------		--------------------------------------------------------------		-----------------------
RF004 - Seções	 
  FLUXO PRINCIPAL
	1.1-Usuário começa a criar solicitação				
	1.2-Usuário usa tags para cumprir requisitos, como qual a natureza do problema e a sua localização (seu departamento)				
	1.3-Se o problema for de algum espaço de departamento ele terá enquente exclusiva para os alunos dele				
	1.4-Apenas alunos do departamento podem votar nas enquetes de seu departamento. 				
	2.1-Uma vez aplicadas as tags nas solicitações, enviadas e aprovadas. As solicitações aparecem para aos usuários podendo ser encontradas pelo filtro de seções.				
	1.6-Somente o DA e os moderadores do CIIU podem alterar os Status das solicitações				
	1.7-O usuário confirma o voto.				
	1.8-O sistema registra o voto e acrescenta uma unidade ao total da opção selecionada.				
	1.9-O sistema exibe o resultado atualizado da enquete.				
	1.10-A enquete e as demais páginas são apresentadas com a estilização definida para o site.				
	FLUXOS ALTERNATIVOS E DE ERRO				
	1-Usuário já votou na enquete -> Sistema não permite um novo voto e exibe apenas o resultado atual.				
	2-Enquete não vinculada à denúncia -> Sistema não exibe a enquete na tela da denúncia.				
	3-Falha ao registrar o voto -> Sistema exibe "Não foi possível registrar seu voto. Tente novamente".				
	4-Nenhuma opção selecionada -> Sistema exibe "Selecione uma opção antes de confirmar o voto".				
	----------------------------------------------------------------------------------------------------		--------------------------------------------------------------		-----------------------
RF005 - Status	
  FLUXO PRINCIPAL
	1.1-O sistema cria a tabela de enquete no banco de dados.				
	1.2-O sistema vincula a enquete à denúncia correspondente por meio de uma chave estrangeira.				
	1.3-O usuário acessa a tela da denúncia.				
	1.4-O sistema exibe a enquete disponível para votação.				
	1.5-O sistema verifica se o usuário já votou na enquete.				
	1.6-Caso o usuário ainda não tenha votado, ele seleciona uma das opções disponíveis.				
	1.7-O usuário confirma o voto.				
	1.8-O sistema registra o voto e acrescenta uma unidade ao total da opção selecionada.				
	1.9-O sistema exibe o resultado atualizado da enquete.				
	1.10-A enquete e as demais páginas são apresentadas com a estilização definida para o site.				
	FLUXOS ALTERNATIVOS E DE ERRO				
	1-Usuário já votou na enquete -> Sistema não permite um novo voto e exibe apenas o resultado atual.				
	2-Enquete não vinculada à denúncia -> Sistema não exibe a enquete na tela da denúncia.				
	3-Falha ao registrar o voto -> Sistema exibe "Não foi possível registrar seu voto. Tente novamente".				
	4-Nenhuma opção selecionada -> Sistema exibe "Selecione uma opção antes de confirmar o voto".				
