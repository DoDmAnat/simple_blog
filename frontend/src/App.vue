<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-md">
      <a class="navbar-brand" href="/">
        <span style="color: rgb(65, 184, 131)">Simple</span
        ><span style="color: rgb(53, 73, 94)">Blog</span>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown"
        aria-expanded="false"
        aria-label="Переключатель навигации"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="nav nav-pills">
          <li class="nav-item">
            <a
              class="nav-link {% if view_name == 'posts:post_create' %}active{% endif %}"
              href=""
            >
              Новая запись
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">Выйти</a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link {% if view_name == 'users:login' %}active{% endif %}"
              href=""
            >
              Вход
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link {% if view_name == 'users:signup' %}active{% endif %}"
              href=""
            >
              Регистрация
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
