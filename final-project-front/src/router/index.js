import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleNewView from '@/views/ArticleNewView'
import ArticleEditView from '@/views/ArticleEditView'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileEditView from '@/views/ProfileEditView.vue'
import NotFound404 from '../views/NotFound404.vue'

import FollowerView from '../views/FollowerView.vue'
import FollowingView from '../views/FollowingView.vue'
import LikeArticleView from '../views/LikeArticleView.vue'
import LikeMovieView from '../views/LikeMovieView.vue'

import MovieWorldCupView from '../views/MovieWorldCupView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticleListView
  },
  {
    path: '/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/profile/:username/edit',
    name: 'profileEdit',
    component: ProfileEditView
  },
  {
    path: '/profile/:username/followers',
    name: 'followers',
    component: FollowerView,
  },
  {
    path: '/profile/:username/followings',
    name: 'followings',
    component: FollowingView,
  },
  {
    path: '/profile/:username/likearticles',
    name: 'likearticles',
    component: LikeArticleView,
  },
  {
    path: '/profile/:username/likemovies',
    name: 'likemovies',
    component: LikeMovieView,
  },
  {
    path : '/movie/movie_worldcup',
    name : 'movie_worldcup',
    component : MovieWorldCupView,
  },
  {
    path: '/movie/:moviePk',
    name: 'movieDetail',
    
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router