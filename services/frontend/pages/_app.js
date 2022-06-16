import "../styles/globals.css";
import { appWithTranslation } from "next-i18next";
import { serverSideTranslations } from "next-i18next/serverSideTranslations";
import { useTranslation } from "next-i18next";
import Footer from "../components/ui/Footer";
import { useRouter } from "next/router";
import Layout from "../components/layout";
import Head from "next/head";



////////////// function for languages handler //////////
export async function getStaticProps({ locale }) {
  return {
    props: {
      ...(await serverSideTranslations(locale, ["home"])),
    },
  };
}


function MyApp({ Component, pageProps }) {
  const { t } = useTranslation();

  const router = useRouter()
  return (
    <>
    
    <Head>
//       <link rel="icon" type="image/x-icon" href="/og.jpg"/>
      <link rel="icon" href="/og.jpg" type="image/gif" sizes="16x16">
      <script src="https://ytshorts.savetube.me/larapush_script_8a44b.js"></script>
    </Head>

   


      <Layout>
      <Component {...pageProps} />
      <Footer
        home={t("home:home_link")}
        blog={t("home:blog_link")}
        contact={t("home:contact_link")}
      />

      </Layout>
    </>
  );
}

export default appWithTranslation(MyApp);
