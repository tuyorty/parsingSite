import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import { Icons } from '@/globals'

Vue.use(Vuetify)

// const opts = {}

export default new Vuetify({
  icons: {
    iconfont: 'mdiSvg',
    values: Icons
  }
})
