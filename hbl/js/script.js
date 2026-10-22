/* ==========================================
   HBL GEOTECH
   JavaScript principal do site
========================================== */

document.addEventListener("DOMContentLoaded", function () {

    /* ==========================================
       1. MENU RESPONSIVO
    ========================================== */

    const menuToggle = document.querySelector(".menu-toggle");
    const menu = document.querySelector("#menu-principal");

    if (menuToggle && menu) {

        // Abre e fecha o menu no celular
        menuToggle.addEventListener("click", function () {

            const menuAberto = menu.classList.toggle("menu-aberto");

            menuToggle.setAttribute(
                "aria-expanded",
                String(menuAberto)
            );

            menuToggle.setAttribute(
                "aria-label",
                menuAberto ? "Fechar menu" : "Abrir menu"
            );

        });

        // Fecha o menu quando um link é selecionado
        const linksMenu = menu.querySelectorAll("a");

        linksMenu.forEach(function (link) {

            link.addEventListener("click", function () {

                menu.classList.remove("menu-aberto");

                menuToggle.setAttribute("aria-expanded", "false");
                menuToggle.setAttribute("aria-label", "Abrir menu");

            });

        });

        // Fecha o menu quando o usuário clica fora dele
        document.addEventListener("click", function (event) {

            const clicouNoMenu = menu.contains(event.target);
            const clicouNoBotao = menuToggle.contains(event.target);

            if (!clicouNoMenu && !clicouNoBotao) {

                menu.classList.remove("menu-aberto");

                menuToggle.setAttribute("aria-expanded", "false");
                menuToggle.setAttribute("aria-label", "Abrir menu");

            }

        });

        // Fecha o menu com a tecla Escape
        document.addEventListener("keydown", function (event) {

            if (event.key === "Escape") {

                menu.classList.remove("menu-aberto");

                menuToggle.setAttribute("aria-expanded", "false");
                menuToggle.setAttribute("aria-label", "Abrir menu");

                menuToggle.focus();

            }

        });

    }


    /* ==========================================
       2. NAVEGAÇÃO SUAVE
    ========================================== */

    const linksInternos = document.querySelectorAll('a[href*="#"]');

    linksInternos.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const href = link.getAttribute("href");

            // Ignora links vazios ou que contenham apenas #
            if (!href || href === "#") {
                return;
            }

            let destino;

            try {
                destino = new URL(href, window.location.href);
            } catch (erro) {
                return;
            }

            // Só trata links que apontam para a página atual
            if (
                destino.origin !== window.location.origin ||
                destino.pathname !== window.location.pathname ||
                !destino.hash
            ) {
                return;
            }

            const id = decodeURIComponent(
                destino.hash.substring(1)
            );

            const secao = document.getElementById(id);

            if (secao) {

                event.preventDefault();

                secao.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

                // Atualiza a URL sem provocar um salto na página
                history.replaceState(null, "", destino.hash);

            }

        });

    });


    /* ==========================================
       3. ANO AUTOMÁTICO NO RODAPÉ
    ========================================== */

    const elementoAno = document.getElementById("ano-atual");

    if (elementoAno) {
        elementoAno.textContent = new Date().getFullYear();
    }


    /* ==========================================
       4. BOTÃO VOLTAR AO TOPO
    ========================================== */

    const botaoTopo = document.querySelector(".voltar-topo");

    if (botaoTopo) {

        botaoTopo.addEventListener("click", function (event) {

            const href = botaoTopo.getAttribute("href");

            // Só intercepta o link se apontar para o início da página atual
            if (href === "#inicio") {

                const inicio = document.getElementById("inicio");

                if (inicio) {

                    event.preventDefault();

                    inicio.scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });

                }

            }

        });

    }


    /* ==========================================
       5. PROTEÇÃO PARA IMAGENS COM ERRO
    ========================================== */

    const imagens = document.querySelectorAll("img");

    imagens.forEach(function (imagem) {

        imagem.addEventListener("error", function () {

            // Evita repetir tentativas em uma imagem que já falhou
            if (imagem.dataset.erroTratado === "true") {
                return;
            }

            imagem.dataset.erroTratado = "true";

            // Se a imagem tiver um fallback definido no HTML,
            // deixa o navegador executar esse comportamento.
            // Caso contrário, apenas registra o estado no elemento.
            imagem.classList.add("imagem-indisponivel");

        });

    });

});