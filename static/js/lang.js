var TRANSLATIONS = {
  uz: {
    hero_title: "Sizning muammoingizga eng tezkor yechim",
    hero_text: "Professional xizmat, ishonchli hamkorlik va sizga mos individual yondashuv.",
    hero_btn: "Murojaat qoldirish",
    feat1_title: "Tezkor xizmatlar",
    feat1_text: "Eng yaxshi shifokorlar va zamonaviy uskunalar.",
    feat2_title: "Ishonchli",
    feat2_text: "Salomatlik va farovonlik yo'lidagi ishonchli hamkoringiz",
    feat3_title: "Yuqori malakali mutaxassislar",
    feat3_text: "Noyob va ko'p yillik tajribaga ega g'amxo'r professionallar",
    form_title: "Murojaat qoldiring",
    form_sub: "Barcha maydonlarni to'ldiring, biz tez orada siz bilan bog'lanamiz.",
    label_name: "Ism *",
    label_phone: "Telefon *",
    label_email: "Email *",
    label_msg: "Xabar (ixtiyoriy)",
    ph_name: "Ismingiz",
    ph_phone: "+998 __ ___ __ __",
    ph_email: "email@example.com",
    ph_msg: "Savolingiz yoki xabaringiz...",
    btn_submit: "Yuborish",
    success: "Murojaatingiz qabul qilindi! Tez orada siz bilan bog'lanamiz.",
    footer_about: "Professional xizmat va ishonchli hamkorlik.",
    footer_contact: "Bog'lanish",
    footer_address: "Manzil",
    footer_city: "100047 Toshkent shaxar, Yashnobod tumani., 2-tor Taraqqiyot ko’chasi 12a-uy",
    copyright: "2026 Temir yo'l markaziy klinik kasalxonasi. Barcha huquqlar himoyalangan."
  },
  ru: {
    hero_title: "Быстрое решение вашей проблемы",
    hero_text: "Профессиональный сервис, надёжное партнёрство и индивидуальный подход.",
    hero_btn: "Оставить заявку",
    feat1_title: "Быстрое обслуживание",
    feat1_text: "Лучшие врачи и современное оборудование",
    feat2_title: "Надежность",
    feat2_text: "Ваш надежный партнер на пути к здоровью и благополучию",
    feat3_title: "Высококвалифицированные специалисты",
    feat3_text: "Заботливые профессионалы с уникальным и многолетним опытом",
    form_title: "Оставьте заявку",
    form_sub: "Заполните все поля, мы свяжемся с вами в ближайшее время.",
    label_name: "Имя *",
    label_phone: "Телефон *",
    label_email: "Email *",
    label_msg: "Сообщение (необязательно)",
    ph_name: "Ваше имя",
    ph_phone: "+998 __ ___ __ __",
    ph_email: "email@example.com",
    ph_msg: "Ваш вопрос или сообщение...",
    btn_submit: "Отправить",
    success: "Ваша заявка принята! Мы свяжемся с вами в ближайшее время.",
    footer_about: "Профессиональный сервис и надёжное партнёрство.",
    footer_contact: "Контакты",
    footer_address: "Адрес",
    footer_city: "100047 г.Ташкент, Яшнабадский район, 2-й переулок, улица Тараккиет, 12а",
    copyright: "2026 Центральная железнодорожная клиническая больница. Все права защищены."
  },
  en: {
    hero_title: "The fastest solution to your problem",
    hero_text: "Professional service, reliable partnership and personalized approach.",
    hero_btn: "Leave a request",
    feat1_title: "Fast services",
    feat1_text: "The best doctors and modern equipment",
    feat2_title: "Reliable",
    feat2_text: "Your reliable partner on the path to health and well-being",
    feat3_title: "Highly qualified specialists",
    feat3_text: "Caring professionals with unique and many years of experience",
    form_title: "Leave a request",
    form_sub: "Fill in all fields, we will contact you soon.",
    label_name: "Name *",
    label_phone: "Phone *",
    label_email: "Email *",
    label_msg: "Message (optional)",
    ph_name: "Your name",
    ph_phone: "+998 __ ___ __ __",
    ph_email: "email@example.com",
    ph_msg: "Your question or message...",
    btn_submit: "Submit",
    success: "Your request has been received! We will contact you soon.",
    footer_about: "Professional service and reliable partnership.",
    footer_contact: "Contact",
    footer_address: "Address",
    footer_city: "100047 Tashkent city, Yashnabad district, 2nd lane, Taraqqiyot street, 12a",
    copyright: "2026 The Railway central clinical hospital. All rights reserved."
  }
};

function applyLang(lang) {
  var t = TRANSLATIONS[lang];
  if (!t) return;
  localStorage.setItem("lang", lang);

  var el;
  el = document.querySelector(".hero h1");        if (el) el.textContent = t.hero_title;
  el = document.querySelector(".hero p");          if (el) el.textContent = t.hero_text;
  el = document.querySelector(".hero .btn-primary"); if (el) el.textContent = t.hero_btn;

  var ft = document.querySelectorAll(".feature-title");
  var fx = document.querySelectorAll(".feature-text");
  if (ft[0]) ft[0].textContent = t.feat1_title;
  if (fx[0]) fx[0].textContent = t.feat1_text;
  if (ft[1]) ft[1].textContent = t.feat2_title;
  if (fx[1]) fx[1].textContent = t.feat2_text;
  if (ft[2]) ft[2].textContent = t.feat3_title;
  if (fx[2]) fx[2].textContent = t.feat3_text;

  el = document.querySelector(".form-title");    if (el) el.textContent = t.form_title;
  el = document.querySelector(".form-subtitle"); if (el) el.textContent = t.form_sub;

  var labels = document.querySelectorAll(".field label");
  var lk = ["label_name","label_phone","label_email","label_msg"];
  labels.forEach(function(el, i) { if (lk[i]) el.textContent = t[lk[i]]; });

  var inputs = [
    document.querySelector("[name=name]"),
    document.querySelector("[name=phone]"),
    document.querySelector("[name=email]"),
    document.querySelector("[name=message]")
  ];
  var pk = ["ph_name","ph_phone","ph_email","ph_msg"];
  inputs.forEach(function(el, i) { if (el && pk[i]) el.placeholder = t[pk[i]]; });

  var sbtn = document.querySelector(".btn-submit");
  if (sbtn && !sbtn.disabled) sbtn.textContent = t.btn_submit;

  el = document.querySelector(".footer-about-text"); if (el) el.textContent = t.footer_about;
  el = document.querySelector(".footer-contact-title"); if (el) el.textContent = t.footer_contact;
  el = document.querySelector(".footer-addr-title"); if (el) el.textContent = t.footer_address;
  el = document.querySelector(".footer-city"); if (el) el.textContent = t.footer_city;
  el = document.querySelector(".footer-bottom"); if (el) el.textContent = "© " + t.copyright;
}

document.addEventListener("DOMContentLoaded", function() {
  var savedLang = localStorage.getItem("lang") || "uz";

  document.querySelectorAll(".lang-btn").forEach(function(btn) {
    btn.classList.remove("active");
    if (btn.dataset.lang === savedLang) btn.classList.add("active");

    btn.addEventListener("click", function() {
      document.querySelectorAll(".lang-btn").forEach(function(b) { b.classList.remove("active"); });
      this.classList.add("active");
      applyLang(this.dataset.lang);
    });
  });

  applyLang(savedLang);
});