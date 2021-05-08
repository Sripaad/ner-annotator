<template>
  <div class="vue-container">
    <button
      class="button is-link"
      @click="$store.commit('setCurrentPage', 'start')"
    >
      Back
    </button>
    <br />
    <h1>Text classification page</h1>

    <br />
    <div class="input-area">
      <textarea class="textarea" v-model="sentence" placeholder="Prompt text" />

      <textarea
        class="textarea"
        v-model="classificationData.Highest_emotion"
        placeholder="Highest emotion"
        disabled
      />
    </div>

    <div class="input-area mt">
      <button class="button is-danger is-outlined" @click="resetBlocks">
        Reset
      </button>
      <button class="button" @click="classifyCurrentSentence">Classify</button>
      <button class="button is-link" @click="saveTags">Save</button>
      <button class="button is-link" @click="exportJson">Export</button>
    </div>
    <!-- {{ tags }} -->
  </div>
</template>

<script>
/* eslint-disable no-mixed-spaces-and-tabs */


import axios from "../axios";


export default {
  name: "TextClassificationPage",
  data: function () {
    return {
      classificationData: {},
      sentence: "",
      tags: [],
    };
  },
  methods: {
    saveTags() {
      this.tags.push(this.classificationData);
      console.log(this.tags);
    },

    resetBlocks() {
      // this.tm.resetBlocks();
      this.sentence = null;
    },

    classifyCurrentSentence() {
      axios
        .post("/api/classify", {
          sentence: this.sentence,
        })
        .then((response) => {
          this.classificationData = response.data;
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    exportJson() {
      const data = JSON.stringify(this.tags);
      const blob = new Blob([data], { type: "text/plain" });
      const e = document.createEvent("MouseEvents"),
        a = document.createElement("a");
      a.download = "classification.json";
      a.href = window.URL.createObjectURL(blob);
      a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");
      e.initEvent(
        "click",
        true,
        false,
        window,
        0,
        0,
        0,
        0,
        0,
        false,
        false,
        false,
        false,
        0,
        null
      );
      a.dispatchEvent(e);
    },
  },
};
</script>

<style lang="scss">
#editor {
  padding: 1rem;
}
</style>