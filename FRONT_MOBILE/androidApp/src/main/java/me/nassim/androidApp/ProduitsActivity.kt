package me.nassim.androidApp

import android.content.Context
import android.os.AsyncTask
import android.os.Bundle
import android.os.PersistableBundle
import android.widget.ListView
import androidx.appcompat.app.AppCompatActivity
import org.json.JSONArray
import java.io.IOException
import java.net.HttpURLConnection
import java.net.URL

class ProduitsActivity: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?, persistentState: PersistableBundle?) {
        super.onCreate(savedInstanceState, persistentState)
        setContentView(R.layout.activity_produits)

        val url = "localhost"

        AsyncTaskHandleJson().execute(url)
    }

    inner class AsyncTaskHandleJson : AsyncTask<String, String, String>() {
        override fun doInBackground(vararg url: String?): String {

            var text: String
            val connection = URL(url[0]).openConnection() as HttpURLConnection
            try{
                connection.connect()
                text = connection.inputStream.use { it.reader().use{reader -> reader.readText()} }
            }
            finally {
                connection.disconnect()
            }

            return text
        }

        override fun onPostExecute(result: String?) {
            super.onPostExecute(result)
            handleJson(result)
        }
    }

    private fun handleJson(jsonString: String?) {

        val jsonArray = JSONArray(jsonString)

        val listProduits = ArrayList<Produits>()

        for(i in 0 until jsonArray.length() ){
            val jsonObject = jsonArray.getJSONObject(i)

            listProduits.add(Produits(
                jsonObject.getInt("id"),
                jsonObject.getString("name")
                ))
        }

        val adapter = ListAdaptProduits(this,listProduits)
        this.findViewById<ListView>(R.id.presidents_list).adapter = adapter

    }
}