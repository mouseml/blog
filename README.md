# мыш блог

Это репозиторий [блога](https://mouseml.github.io/blog) с постами по видео на канале [мыш](https://www.youtube.com/channel/UCscWjyvPudzdIaGCCtEL3nw).

Я мог сделать ошибки в постах, поэтому буду рад, если вы поможете их найти. Об ошибках можно сообщить в [Telegram](https://t.me/ml_mouse), через [GitHub Issue](https://github.com/mouseml/blog/issues) или [Pull Request](https://github.com/mouseml/blog/pulls).

Я слежу за вами через Google Analytics. Так я могу узнать, какие посты вы чаще читаете и сколько времени проводите на странице. Это помогает мне делать посты полезнее.

## Разработка

Блог собран на [Astro](https://astro.build), пакетный менеджер — [Bun](https://bun.sh). Установить Bun можно по [этой инструкции](https://bun.sh/docs/installation). Установите зависимости:

```shell
bun install
```

Запустите блог локально с горячей перезагрузкой:

```shell
bun run dev
```

Перед публикацией можно собрать продакшен-версию (Astro + полнотекстовый поиск Pagefind):

```shell
bun run build
```

Так можно внести изменения и проверить окончательный вариант страниц перед публикацией.
