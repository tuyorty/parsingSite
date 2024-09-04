<template>
  <v-container
    class="d-flex align-center justify-center"
    fill-height
  >
    <v-sheet
      class="mx-auto"
      width="300"
      elevation="12"
      rounded="lg"
      color="#D8EFD3"
    >

    <h2 class="d-flex font-weight-bold mb-6 justify-center">Parsing Site</h2>

      <p class="d-flex font-weight-bold justify-center">Ссылка на сайт</p>

      <form ref="form" class="ma-3">
        <v-text-field
          v-model="URL"
          label="URL"
          required
        ></v-text-field>

        <p class="d-flex font-weight-bold justify-center">Какой блок парсим</p>

        <v-row>
          <v-col>
            <v-text-field
              v-model="htmlElementBlock"
              label="HTML Element"
              required
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="classElementBlock"
              label="Class"
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <p class="d-flex font-weight-bold justify-center">Название</p>

        <v-row>
          <v-col>
            <v-text-field
              v-model="htmlElementTitle"
              label="HTML Element"
              required
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="classElementTitle"
              label="Class"
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <p class="d-flex font-weight-bold justify-center">Цена</p>

        <v-row>
          <v-col>
            <v-text-field
              v-model="htmlElementPrice"
              label="HTML Element"
              required
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="classElementPrice"
              label="Class"
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <p class="d-flex font-weight-bold justify-center">Ссылка</p>

        <v-row>
          <v-col>
            <v-text-field
              v-model="htmlElementLink"
              label="HTML Element"
              required
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="classElementLink"
              label="Class"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <div class="d-flex flex-column">
          <v-btn class="mt-4" color="#ADD899" block @click="validate">
            Лезем
          </v-btn>

          <v-btn class="mt-4" color="#FF6969" block @click="reset">
            Еще разок
          </v-btn>
        </div>
      </form>

      <!-- Отображение результатов -->
      <v-list v-if="results.length" class="mt-5" color="#D8EFD3">
        <v-list-item-group>
          <v-list-item
            v-for="(item, index) in results"
            :key="index"
          >
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
              <v-list-item-subtitle>{{ item.price }}</v-list-item-subtitle>
              <v-list-item-action>
                <v-btn :href="'https://www.avito.ru' + item.link" target="_blank">
                  Перейти
                </v-btn>
              </v-list-item-action>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-sheet>
  </v-container>
</template>

<script lang="ts">
import { Component } from 'vue-property-decorator'
import Vue from 'vue'

interface Item {
  title: string;
  price: string;
  link: string;
}

@Component({
  components: {

  }
})

export default class MainWindow extends Vue {
  URL = ''
  htmlElementBlock = ''
  classElementBlock = ''
  htmlElementTitle = ''
  classElementTitle = ''
  htmlElementPrice = ''
  classElementPrice = ''
  htmlElementLink = ''
  classElementLink = ''
  results: Item[] = []

  validate () {
    // Формируем данные для отправки на бэк
    const data = {
      URL: this.URL,
      htmlElementBlock: this.htmlElementBlock,
      classElementBlock: this.classElementBlock,
      htmlElementTitle: this.htmlElementTitle,
      classElementTitle: this.classElementTitle,
      htmlElementPrice: this.htmlElementPrice,
      classElementPrice: this.classElementPrice,
      htmlElementLink: this.htmlElementLink,
      classElementLink: this.classElementLink
    }

    // Отправляем данные на бэк
    fetch('http://127.0.0.1:5000/parse', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(result => {
        console.log('Result:', result)
        this.results = result
      })
      .catch(error => {
        console.error('Error:', error)
      })
  }

  reset () {
    this.URL = ''
    this.htmlElementBlock = ''
    this.classElementBlock = ''
    this.htmlElementTitle = ''
    this.classElementTitle = ''
    this.htmlElementPrice = ''
    this.classElementPrice = ''
    this.htmlElementLink = ''
    this.classElementLink = ''
    this.results = []
  }
}
</script>
