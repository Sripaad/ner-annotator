<template>
  <div class="vue-container">
    <button
      class="button is-link"
      @click="$store.commit('setCurrentPage', 'start')"
    >
      Back
    </button>
    <br>
    <br>
    <br>
    <section class="hero is-dark">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Text Generation</h1>
          <h2 class="subtitle">Generate Sequence of text.</h2>
        </div>
      </div>
    </section>  
    <br>
    <br>
    <br>
    <br>
    <div class="input-area">
      <textarea
        class="textarea"
        v-model="prompt_text"
        placeholder="Prompt text"
      />
      <textarea
        class="textarea"
        v-model="generated_sequence.generated_text"
        placeholder="Generated text"
        disabled
      />
    </div>
    <br>
    <br>
    <br>
    <br>
    <div class="input-area mt">
      <button class="button is-danger is-outlined" @click="resetBlocks">
        Reset
      </button>
      <button class="button" @click="generateSequences">Generate</button>
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
  name: "SequenceGenerationPage",
  data: function () {
    return {
      prompt_text: "",
      redone: "",
      generated_text: "",
      generated_sequence: {},
      tags: [],
    };
  },
  methods: {
    saveTags() {
      this.tags.push({prompt_text: this.prompt_text, generated_text: this.generated_text})
      console.log(this.tags);
    },

    resetBlocks() {
      this.prompt_text = null;
    },

    generateSequences() {
      axios
        .post("/api/generate", {
          prompt_text: this.prompt_text,
        })
        .then((response) => {
          this.generated_sequence = response.data;
          console.log(response);
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
      a.download = "sequence.json";
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
.vue-container {
  padding: 20px;
}
.input-area {
  display: flex;
  justify-content: center;
  gap: 10px;
}
.textarea {
  max-width: unset !important;
  min-width: unset !important;
}
.mt {
  margin-top: 10px;
}
</style>