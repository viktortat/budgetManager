<template>
  <transition
    name="modal"
    appear>
    <div
      v-if="visible"
      class="modal-wrapper"
      @click.self="hide">
      <div class="modal-body">
        <p class="modal-title">{{ title }}</p>
        <p
          class="modal-message"
          v-html="message"/>
        <div class="modal-buttons">
          <app-button
            class="button"
            @click="hide">Zrušit</app-button>
          <app-button
            v-if="showConfirmButton"
            class="button is-danger"
            @click="confirmFunction">{{ confirmButtonText }}</app-button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { Modal } from "@/plugins";

import AppButton from "@/components/AppButton.vue";

export default {
  components: { AppButton },
  data() {
    return {
      visible: false,
      title: "",
      message: "",
      showConfirmButton: false,
      confirmButtonText: "Potvrdit",
      onConfirm: {}
    };
  },
  beforeMount() {
    Modal.EventBus.$on("show", params => {
      this.show(params);
    });
  },
  methods: {
    show(params) {
      this.visible = true;
      if (params) {
        this.title = typeof params.title === "string" ? params.title : "";
        this.message = typeof params.message === "string" ? params.message : "";
        this.showConfirmButton =
          typeof params.showConfirmButton === "boolean"
            ? params.showConfirmButton
            : false;
        this.onConfirm =
          typeof params.onConfirm === "function" ? params.onConfirm : {};
        this.confirmButtonText =
          typeof params.confirmButtonText === "string"
            ? params.confirmButtonText
            : "Potvrdit";
      }
    },
    hide() {
      this.reset();
      this.visible = false;
    },
    reset() {
      this.title = "";
      this.message = "";
      this.showConfirmButton = false;
      (this.onConfirm = {}), (this.confirmButtonText = "Potvrdit");
    },
    confirmFunction() {
      if (typeof this.onConfirm === "function") {
        this.onConfirm();
        this.hide();
      } else {
        this.hide();
      }
    }
  }
};
</script>

<style lang="stylus" scoped>
@import '../styles/variables'

.modal-wrapper
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    z-index: 8000

    background-color: rgba(0, 0, 0, 0.2)

.modal-body
    @media screen and (max-width: 500px)
        width: calc(100% - 5px)

    position: absolute
    width: 400px
    padding: 20px
    padding-top: 80px
    padding-bottom: 80px
    top: 50%
    left: 50%

    border-radius: $BORDER-RADIUS
    background-color: #FFFFFF

    transform: translate(-50%, -50%)

.modal-title
    position: absolute
    top: 0
    left: 0
    right: 0
    padding: 20px

    font-size: 1.2em
    font-weight: 600

.modal-message
    padding-bottom: 10px

    line-height: 1.3

.modal-buttons
    display: flex
    justify-content: space-around
    align-items: center
    position: absolute
    bottom: 0
    left: 0
    right: 0
    height: 60px

.modal-enter, .modal-leave-to
    opacity: 0

.modal-enter-active, .modal-leave-active
    transition: opacity 0.3s ease-in-out

</style>
